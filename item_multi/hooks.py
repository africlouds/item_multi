# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "item_multi"
app_title = "Item Multi"
app_publisher = "Africlouds Ltd"
app_description = "Assigning items per company in a multi company set up"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "arwema@gmail.com"
app_license = "MIT"

fixtures = ["Custom Field", "Custom Script"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/item_multi/css/item_multi.css"
# app_include_js = "/assets/item_multi/js/item_multi.js"

# include js, css files in header of web template
# web_include_css = "/assets/item_multi/css/item_multi.css"
# web_include_js = "/assets/item_multi/js/item_multi.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "item_multi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "item_multi.install.before_install"
# after_install = "item_multi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "item_multi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"item_multi.tasks.all"
# 	],
# 	"daily": [
# 		"item_multi.tasks.daily"
# 	],
# 	"hourly": [
# 		"item_multi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"item_multi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"item_multi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "item_multi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "item_multi.event.get_events"
# }

