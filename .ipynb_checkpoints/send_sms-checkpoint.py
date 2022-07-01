def main():
    import boto3
    
    client=boto3.client('sns','ap-southeast-1')


    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait

    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")  
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()

    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyDo6EGuSxW1_iKQRKBrVkgsmVP0x_FrG4c')
    results = gmaps.reverse_geocode((latitude,longitude))
    msg="Warning!! Anomaly Detected \n"+"Location: "+results[0]['formatted_address']
    client.publish(PhoneNumber='+919492449689',Message=msg)


if __name__ == '__main__':
    main()

