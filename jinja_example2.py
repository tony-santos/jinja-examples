from jinja2 import Template

sql_template = Template("""
SELECT
        {{query_id}} AS query_id
{% for column in columns %}
    {% for key in column %}
        ,a.{{key}} AS {{column[key]}}
    {% endfor %}
{% endfor %}
        ,COUNT(1) AS _count
FROM {{table_name}} a
GROUP BY
        1,
{% for column in columns %}
    {% for key in column %}
        ,a.{{key}}
    {% endfor %}
{% endfor %}
""")

sql_template2 = Template("""
SELECT
        {{query_id}} AS query_id
{% for column in columns %}
    {% for key in column %}
        ,a.{{key}} AS {{column[key]}}
    {% endfor %}
{% endfor %}
        ,COUNT(1) AS _count
FROM {{table_name}} a
{% for table in left_joins %}
LEFT JOIN {{table}}
{% if not loop.last %}
    UNION
{% endif %}
{% endfor %}
""")

left_joins = ['standard_units', 'conversion']

columns = [
    'col1',
    'col2'
]

output_template = sql_template.render(
    query_id=102,
    table_name='test_02',
    columns=columns
)

output_template2 = sql_template2.render(
    query_id=102,
    table_name='test_02',
    columns=columns,
    left_joins=left_joins
)
print(output_template2)