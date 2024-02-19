# Annandale
Welcome to the Annandale HTML Components library. I created this library because I needed a way of distributing HTML templates across a number of users of the Anacostia Pipeline. I love Jinja2 templates but I needed a more user-friendly approach to distribute these templates to users of Anacostia.

What I used to do was I packaged the Jinja2 templates into the Anacostia Pipeline package as ```package_data``` and then publish the package onto PyPI. From there, users of Anacostia would have to use the ```pkg_resources``` library to extract the templates from the package and then create their own child templates. The architecture and development philosophy of Anactostia emphasized enabling developers to build their own Anacostia nodes *and* the custom frontend for their nodes. Enabling this development philosophy would require a server-side rendering approach where developers would create a FastAPI sub-application that would interact with their node(s), render the information of the nodes in an html fragment, and then the html fragment would be inserted into the DOM via htmx. This approach was promising but FastAPI presented a problem: only one directory can be defined for the main application, thus, users simply could not just create their own templates directory and then mount their templates directory into their sub-application which would then be recognized by the main application. Therefore, a more user-friendly approach was needed. 

The solution I decided upon was to create a library to render HTML fragments using only python which would not require the use of Jinja2 nor any templating directories that needed to be mounted into the FastAPI sub-application. Distribution of the fragments could be done by packaging the code for the fragments inside the Anacostia Pipeline package where the user could simply import the fragments into their python development environment. From there, the FastAPI sub-applications could simply render the templates during runtime and return the html snippets as the response to htmx requests.

###The Annandale Library:
There are only three important files (i.e., modules) in this library:
#####base.py
There is not much to this library. The ```Component``` class in ```base.py``` is the base class that is responsible for constructing the tag for the element. The ```Component``` class simply takes two arguments ```children``` (a list of child components) and ```attributes``` (a dictionary of HTML attributes to put on the element). The ```Component``` simply recursively calls the ```str()``` function to render all of its child components and then places the attributes into the element.

#####default.py
A library of all of the basic HTML5 elements codified as components.

#####utils.py
A library that provides functionalities such as formatting the rendered HTML into a more aethetically pleasing format. 

###Example Usage:
This is how you can use Annandale to create your own HTML components:
```python
class CustomComponent(Component):
    def __init__(
        self, 
        child1: Union[str, 'Component', List['Component']], 
        child2: Union[str, 'Component', List['Component']], 
        properties: Dict[str, str] = {}
    ) -> None:
        super().__init__([
            div([
                p("Hello, World 1!"),
                child1
            ], {"class": "container"}),
            div([
                p("Hello, World 2!"),
                child2
            ], {"class": "container"})
        ], properties=properties)

    def __str__(self) -> str:
        return super().__str__() 

if __name__ == "__main__":
    component = html([
        head([
            title("Hello, World!"),
            meta({"charset": "UTF-8", "name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
            link({"rel": "stylesheet", "href": "style.css"}),
            script("", {"src": "script.js"})
        ]),
        body([
            CustomComponent(
                p("Hello, World 3!"), 
                p("Hello, World 4!"), 
                {"id": "custom-component1"}
            ),
            CustomComponent(
                p("Hello, World 5!"), 
                p("Hello, World 6!"), 
                {"id": "custom-component2"}
            ),
            script("console.log('Hello, World!');")
        ])
    ])

    print(format_html(component))
```
Output HTML:
```html
<!DOCTYPE html>
<html>
 <head>
  <title>
   Hello, World!
  </title>
  <meta charset="utf-8" content="width=device-width, initial-scale=1.0" name="viewport"/>
  <link href="style.css" rel="stylesheet"/>
  <script src="script.js">
  </script>
 </head>
 <body>
  <customcomponent id="custom-component1">
   <div class="container">
    <p>
     Hello, World 1!
    </p>
    <p>
     Hello, World 3!
    </p>
   </div>
   <div class="container">
    <p>
     Hello, World 2!
    </p>
    <p>
     Hello, World 4!
    </p>
   </div>
  </customcomponent>
  <customcomponent id="custom-component2">
   <div class="container">
    <p>
     Hello, World 1!
    </p>
    <p>
     Hello, World 5!
    </p>
   </div>
   <div class="container">
    <p>
     Hello, World 2!
    </p>
    <p>
     Hello, World 6!
    </p>
   </div>
  </customcomponent>
  <script>
   console.log('Hello, World!');
  </script>
 </body>
</html>
```
Example usage #2:
```python
fragments = format_html([
    CustomComponent(
        p("Hello, World 3!"), 
        p("Hello, World 4!"), 
        {"id": "custom-component1"}
    ),
    CustomComponent(
        p("Hello, World 5!"), 
        p("Hello, World 6!"), 
        {"id": "custom-component2"}
    )
])
print(fragments)
```
Output:
```html
<customcomponent id="custom-component1">
 <div class="container">
  <p>
   Hello, World 1!
  </p>
  <p>
   Hello, World 3!
  </p>
 </div>
 <div class="container">
  <p>
   Hello, World 2!
  </p>
  <p>
   Hello, World 4!
  </p>
 </div>
</customcomponent>
<customcomponent id="custom-component2">
 <div class="container">
  <p>
   Hello, World 1!
  </p>
  <p>
   Hello, World 5!
  </p>
 </div>
 <div class="container">
  <p>
   Hello, World 2!
  </p>
  <p>
   Hello, World 6!
  </p>
 </div>
</customcomponent>
```
As you can see, not need for Jinja2 or any templating library necessary. 

Advantages of using Annandale:
1. Extremely lightweight library: ```Annandale``` has only 1 dependency, BeautifulSoup4, that is it.
2. Easy to understand: it is fairly easy to see what HTML code will be generated from Annandale Components. Obviously it is not as easy to see the HTML code that will be created by custom components so as a best practice, create custom components that are simple. In short, create and use custom components at your own peril.
3. No need to create template files: all rendering is done in python code.

#####Jinja2 vs Annandale Comparison:
for loops:
```html
{% for record in records %}
<div id="record.id">{{ record.content }}</div>
{% endfor }
```
```python
format_html(
    [div(record.content, {"id": record.id}) for record in records]
)
```
conditionals:
```html
{% if is_open == True %}
    <button class=".open_btn">open</button>
{% else %}
    <button class=".close_btn">close</button>
{% endif %}
```
```python
format_html(
    button("open", {"class": ".open_btn"}) if is_open is True else button("close", {"class": ".close_btn"})
)
```