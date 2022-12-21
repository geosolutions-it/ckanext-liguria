from ckan.plugins import toolkit as t


def get_groups(max_results=20):
    return _get_featured('group', max_results)


def get_organizations(max_results=20):
    return _get_featured('organization', max_results)


def _get_featured(group_type, max_results):
    params_any = {'limit': max_results, 'all_fields': True}
    call_name = '{}_list'.format(group_type)
    action = t.get_action(call_name)

    data = action({}, params_any)
    return data[:max_results]

