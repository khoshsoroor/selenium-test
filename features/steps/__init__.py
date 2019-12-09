from selenium import webdriver
from aloe import step
from .. import logger
from catalyst import service_invoker
from catalyst.service_invoker import get_swagger_operations
from aloe import before, step, world


@step("GET the URL title")
def start_url(_):
    world.driver = webdriver.Chrome()
    world.driver.get("https://dev.ostadkar.pro")
    logger.info(world.driver.get("https://dev.ostadkar.pro"))


@step("I have logged into the system")
def log_in(_):
    assert "Ostadkar Web App" in world.driver.title
    elem = world.driver.find_element_by_css_selector('button.ods-btn  btn-small ods-btn__ghost')
    logger.info(elem)

