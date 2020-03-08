import jinja2 as jinja

template1 = """
{%- macro generate_text(val) -%}
    This template does nothing but print boilerplate + {{val}}
{%- endmacro %}
"""

env = jinja.Environment()
env.globals['generate_text'] = env.from_string(template1).module.generate_text
template_ref = '{{ generate_text(val) }}'

txt1 = env.from_string(template_ref).render(val=4)
txt2 = env.from_string(template_ref).render(val='this text passed into the template')

print(f"txt1 = {txt1}")
print(f"txt2 = {txt2}")
# print(f"type(txt) = {type(txt)}")
