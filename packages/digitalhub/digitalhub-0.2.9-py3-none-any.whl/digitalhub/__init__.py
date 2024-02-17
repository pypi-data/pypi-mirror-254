from digitalhub_core import (
    delete_artifact,
    delete_function,
    delete_project,
    delete_run,
    delete_task,
    delete_workflow,
    get_artifact,
    get_function,
    get_run,
    get_task,
    get_workflow,
    import_artifact,
    import_function,
    import_run,
    import_task,
    import_workflow,
    new_artifact,
    new_function,
    new_run,
    new_task,
    new_workflow,
    set_dhub_env,
    set_store,
    update_artifact,
    update_function,
    update_project,
    update_run,
    update_task,
    update_workflow,
)

_project_imported = False
try:
    from digitalhub_data import (
        delete_dataitem,
        get_dataitem,
        get_or_create_project,
        get_project,
        import_dataitem,
        import_project,
        new_dataitem,
        new_project,
        update_dataitem,
    )

    _project_imported = True
except ImportError:
    raise

if not _project_imported:
    from digitalhub_core import get_or_create_project, get_project, import_project, new_project
