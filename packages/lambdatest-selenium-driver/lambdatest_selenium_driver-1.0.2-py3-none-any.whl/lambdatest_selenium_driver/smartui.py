import json
from lambdatest_sdk_utils import is_smartui_enabled,fetch_dom_serializer,post_snapshot
from lambdatest_sdk_utils import get_pkg_name,setup_logger,get_logger


def smartui_snapshot(driver, name,options={}):
    # setting up logger
    setup_logger()
    logger = get_logger()
    
    try:
        if not name:
            raise Exception('The `snapshotName` argument is required.')
        if is_smartui_enabled() is False: 
            raise Exception("Cannot find SmartUI server.")
        
        resp = fetch_dom_serializer()
        driver.execute_script(resp['data']['dom'])

        # Serialize and capture the DOM
        dom = driver.execute_script(
            f"""
            return {{
                dom: SmartUIDOM.serialize({json.dumps(options)}),
                url: document.URL
            }}
            """
        )

        # Post the dom to smartui endpoint
        dom['name'] = name
        res = post_snapshot(dom,get_pkg_name(),options=options)

        if res and res.get('data') and res['data'].get('warnings') and len(res['data']['warnings']) != 0:
            for warning in res['data']['warnings']:
                logger.warn(warning)

        logger.info(f'Snapshot captured {name}')
    except Exception as e:
        logger.error(f'Could not take snapshot "{name}" Error {e}')