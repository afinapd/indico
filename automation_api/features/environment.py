def before_all(context):
    """Initialize test environment before all tests"""
    pass

def after_all(context):
    """Clean up after all tests"""
    pass

def before_scenario(context, scenario):
    """Initialize scenario-specific resources"""
    pass

def after_scenario(context, scenario):
    """Clean up any resources after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.delete_all_cookies()
