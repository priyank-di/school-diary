cd school_diary/templates
name=""
read -p "Enter name of the file: " name
name="${name}.html"
cat <<EOT >> $name
{% extends 'base/base.html' %}
{% load static %}

{% block title %}
<title></title>
{% endblock %}

{% block css %}
{% endblock %}

{% block content %}
<div class="container">

</div>
{% endblock %}
EOT
echo "done"