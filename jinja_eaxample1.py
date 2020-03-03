from jinja2 import Template
t1 = Template("Hello {{something}}")
print(t1.render(something="World!"))

t2 = Template("My favorite numbers: {% for n in range(1,10) %}{{loop.index0}} {{loop.revindex0}} {{loop.first}} {{loop.last}}" " {% endfor %}")
print(t2.render())


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
t3 = Template("A look at some index values: {% for item in list1 %} {{item}} {{loop.index, loop.index0, loop.revindex, loop.revindex0}} " " {% endfor %}")
print(t3.render())

columns = ['col1', 'col2', 'col3']
sql_template = Template("""
{% for column in columns %}
    '\nleft join {{n}}'
    '\non {{column}}'
    {% if not loop.last %}
        '\nunion'
    {% endif %}
{% endfor %}
""")

print(sql_template.render())
