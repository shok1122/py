/**
 * @file {{struct}}.h
 * @date {{date}}
 */

#ifndef {{define}}
#define {{define}}

struct {{struct}}
{
{%- for member in member_list %}
	{{member.type}} {{member.name}}; ///< {{member.comment}}
{%- endfor %}
}

#endif /* {{define}} */
