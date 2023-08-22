from dagster import solid


@solid
def get_name():
    return "Kan"
