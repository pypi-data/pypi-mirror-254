import argparse
import logging
import pathlib
import sys
import datetime
import json
from jinja2schema import infer
from pathlib import Path
from typing import Generator
from jinja2 import Environment, FileSystemLoader

from tinyscaf.util.logging_config import configure_logging

logger = logging.getLogger(__name__)
today = datetime.date.today()


def fetch_args():
    """
    Sets up command line arguments.
    Returns: object: instance of argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config_file",
        help="Path to config file. Overrides automatically finding the config file under the current directory.",
        default=None,
    )
    parser.add_argument(
        "-v", "--verbose", help="Verbose", action="store_true", default=False
    )

    return parser


def find_config() -> Path:
    """
    Finds the config file tinyscaf.json starting from the current directory

    :return: pathlib.Path
    """
    current_path = Path.cwd()
    config_file: pathlib.Path = next(Path.rglob(current_path, "tinyscaf.json"), None)
    if config_file:
        logger.debug(f"Found config file at: {config_file}")
        return config_file
    else:
        raise FileNotFoundError(
            f"tinyscaf.json file not found under path: {current_path}."
        )


def load_config(config_file: Path) -> dict:
    """
    Loads the config file and returns a dictionary.

    :param config_file: pathlib.Path
    :return: dict
    """

    if config_file.is_file():
        with open(config_file, "r") as f:
            config_dict = json.load(f)
        return config_dict
    else:
        raise FileNotFoundError(f"{config_file} does not exist!")


def get_templates(template_dir: Path) -> Generator[Path, None, None]:
    """
    Finds all jinja2 templates in the directory where the tinyscaf.json file lives.
    Templates must reside in the same folder as the tinyscaf.json.

    :param template_dir: pathlib.Path
    :return: Generator[Path, None, None]
    """
    found_templates = Path.glob(template_dir, "*.jinja")
    if found_templates:
        return found_templates
    else:
        raise FileNotFoundError(f"No templates found at: {template_dir}")


def display_multi_choice(question: str, items: list) -> str:
    """
    Displays a list of enumerated items that can be chosen
    by their int index.

    :param question: str
    :param items: list
    :return: str
    """
    choice_string = f"{question} "
    item_enum = enumerate(items)
    item_list: str = "Choices: \n"
    for count, value in item_enum:
        item_list = f"{item_list} \n{count} - {value}"
    print(f"{item_list}")
    choice_int = input(f"{choice_string} ")

    return items[int(choice_int)]


def handle_user_choice(choice: int, items: list) -> list|None:
    """
    Returns the chosen item

    :param choice: int
    :param items: list
    :return: list | None
    """
    if choice.is_integer():
        choice_number = int(choice)
        if 1 <= choice_number <= len(items):
            return items[choice_number - 1]
    return None


def ask_questions(template_file_name: str, config_dict: dict) -> dict:
    """
    Asks questions for the chosen template and updates the dictionary with the
    answers populated.

    :param template_file_name: str
    :param config_dict: dict
    :return: dict
    """
    questions: dict = [
        x for x in config_dict if x["template_name"] == template_file_name
    ][0]
    logger.debug(f"Asking questions for template: {template_file_name}")
    for key, question in questions.items():
        if not key == "template_name" and not key == "file_name":
            answer = input(f"{question} ")
            questions[key] = answer

    return {"tinyscaf": questions}


def ask_filename(questions: dict) -> dict:
    """
    Adds or updates the file_name key to the dictionary with the filename or formatted file name
    from the tinyscaf.json config.

    :param questions: dict
    :return: dict
    """
    if "file_name" not in questions["tinyscaf"]:
        filename = input("Save file as: ")
        questions["tinyscaf"]["file_name"] = filename
    else:
        filename_template = questions["tinyscaf"]["file_name"]
        file_name = filename_template.format(**questions["tinyscaf"])
        location = input(
            f"File name will be: {file_name} - Specify the directory to save to. Leave blank for working dir. "
        )
        questions["tinyscaf"]["file_name"] = pathlib.PurePath(location, file_name)

    return questions


def write_file(
    template_file: Path,
    out_file: Path,
    answers: dict,
) -> None:
    """
    Writes out the final template to the location used for file_name.

    :param template_file: pathlib.Path
    :param out_file: pathlib.Path
    :param answers: dict
    :return: None
    """
    env = Environment(loader=FileSystemLoader(template_file.parent))
    template = env.get_template(template_file.name)
    with open(out_file, "w") as f:
        f.write(template.render(answers))


def main():
    """
    Main entry point, collects arguments and parses before handing control to the runner.

    :return: None
    """
    arguments = fetch_args()
    args = arguments.parse_args()
    run(arguments=args)


def run(arguments):
    """
    Function that controls the program workflow

    :param arguments: argparse collected arguments
    :return: None
    """

    configure_logging(log_level=arguments.verbose)

    # Find or override the tinyscaf.json file
    if arguments.config_file:
        config_file = Path(arguments.config_file)
    else:
        config_file = find_config()

    loaded_config = load_config(config_file=config_file)
    logger.debug(f"Config file dictionary: {loaded_config}")

    # Read the templates in the template directory
    templates: Generator = get_templates(template_dir=config_file.parent)
    template_list: list = []
    for template in templates:
        logger.debug(f"Found template: {template}")
        template_dict = {"filename": template.name, "template_path": template}
        template_list.append(template_dict)
    logger.debug(f"Template info: {template_list}")

    template_files = sorted([x["template_name"] for x in loaded_config])
    logger.debug(template_files)

    # Ask the user which template file to use
    template_choice = display_multi_choice(
        question="Choose a template file:", items=template_files
    )
    logger.debug(f"Template chosen: {template_choice}")
    template_choice_path = [
        x["template_path"] for x in template_list if x["filename"] == template_choice
    ][0]

    template_answers = ask_questions(template_choice, config_dict=loaded_config)
    logger.debug(f"Answers: {template_answers}")

    template_answers = ask_filename(questions=template_answers)
    logger.debug(f"Saving to: {template_answers['tinyscaf']['file_name']} ")

    # Append today's date as a universally available date in all answers
    template_answers["tinyscaf"]["tinyscaf_today"] = today
    write_file(
        template_file=template_choice_path,
        out_file=template_answers["tinyscaf"]["file_name"],
        answers=template_answers,
    )
    logger.info("Finished")


if __name__ == "__main__":
    sys.exit(main())
