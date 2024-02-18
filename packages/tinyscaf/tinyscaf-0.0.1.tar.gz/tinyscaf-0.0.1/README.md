# Tinyscaf 

Tinyscaf is a micro scaffolder for simple files you produce all the time.
It is an easy way to standardize the basic structure of files you use all the time
in projects.

### Installation
    pip install tinyscaf

### Configuration
- Create a directory called **templates**
- Create a configuration file called **tinyscaf.json** inside the templates directory
- Create a jinja2 template file using tinyscaf.<variable_name> for the items you want replaced
- In tinyscaf.json, create a list of objects, one per jinja template
- Populate the json object with the **variable_name** as the key and the value is the question you want to prompt the user with.
- Any matching tinyscaf.<variable_name> will be replaced the in output file

### Example

#### templates/tinyscaf.json

    [
        {
        "template_name": "view.jinja",
        "file_name": "{view_name}.sql",
        "view_name": "What is the name of this view?"
        }
    ]

#### templates/view.jinja

    CREATE VIEW { tinyscaf.view_name } AS
    SELECT order_id, customer_name, total_amount
    FROM orders limit 100;


The **template_name** key in each json object is required to identify the associated template.
If you want to have a file naming standard based on the answer of one of your
questions, you can use the key **file_name** and the value pointing to the variable_name
of the question you want to use in jinja templating formatting.

    [
        {
            "template_name": "function.jinja",
            "function_name": "What is the name of the function?",
            "file_name": "{function_name}.sql"
        }
    ]

### Useage:

From the parent folder of templates run tinyscaf
Tinyscaf will automatically search the templates directorys for the tinyscaf.json file
and any jinja files in the template directory

    $> tinyscaf
    Choices: 
     
    0 - function.jinja 
    1 - view.jinja
    Choose a template file:  1
    What is the name of this view? test_view
    File name will be: test_view.sql - Specify the directory to save to. Leave blank for working dir. 
    $> 2024-02-02 00:32:42,918 [INFO] [tinyscaf:188] - Finished

If you are not in the parent folder of templates, you can override the auto search for tinyscaf.json
and specify the path to the config file manually. Tinyscaf will then search the directory
where the config file lives for any jinja template files.

    $> tinyscaf --config_file ../../templates/tinyscaf.json
    Choices: 
     
    0 - function.jinja 
    1 - view.jinja
    Choose a template file:  1
    What is the name of this view? test_view
    File name will be: test_view.sql - Specify the directory to save to. Leave blank for working dir. 
    $> 2024-02-02 00:32:42,918 [INFO] [tinyscaf:188] - Finished


