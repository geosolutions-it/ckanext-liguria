import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.liguria.helpers as h

class LiguriaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'liguria')  # path, webasset name


    # ITemplateHelpers
    def get_helpers(self):
        return {
            'lig_get_organizations': h.get_organizations,
            'lig_get_groups': h.get_groups,
        }
