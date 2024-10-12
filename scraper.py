import time  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
import chromedriver_autoinstaller  
  
# Setup Chrome Options  
chrome_options = webdriver.ChromeOptions()  
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')  
  
# Install chromedriver if not found  
chromedriver_autoinstaller.install()  
  
def get_first_youtube_video_id(search_query):  
    max_attempts = 3  
    attempt = 0  
    print(search_query,"search_query")
    while attempt < max_attempts:  
        attempt += 1  
        try:  
            with webdriver.Chrome(options=chrome_options) as driver:  
                # Open YouTube search results page  
                search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"  
                driver.get(search_url)  
                time.sleep(3)  # Allow time for the page to load  
  
                # Scroll to load more videos  
                for _ in range(3):  
                    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)  
                    # time.sleep(2)  
  
                # Extract video IDs  
                video_elements = driver.find_elements(by=By.TAG_NAME, value="ytd-video-renderer")  
                for video in video_elements:  
                    href = video.find_element(by=By.ID, value="thumbnail").get_attribute('href')  
                    if href:  
                        video_id = href.split('=')[1]  
                        return video_id  # Return as soon as the first video ID is found  
  
        except Exception as e:  
            print(f"Error: {str(e)}")  
  
        print(f"No video ID found on attempt {attempt}. Retrying...")  
        time.sleep(1)  
  
    return None  # Return None if no video ID found after all attempts  

def fetchvideo(title):
    print("title",title)
    videoIdList=[] 
    video_id = get_first_youtube_video_id(title)  
    if video_id:  
     print(f"Found video ID: {video_id}")  
     videoIdList.append(video_id)
    else:  
     print("No video ID found after maximum attempts.")  
   
    print(videoIdList)
    return videoIdList 