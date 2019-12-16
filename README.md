# Hot-Monkey-Engine (WIP)

Hot-Monkey-Engine is a Python pipelined web-scraping library that revolves around handling JavaScript scraping alongside HTML scraping. Hot-Monkey-Engine wraps around the selenium driver to give an easier to use framework for web-scraping. Hot-Monkey-Engine handles each pipeline item as a 'map-reduce' like sequence where you can 'map' UI data into an object and 'reduce' the data from it. However, unlike other web-scraping libraries, Hot-Monkey-Engine handles the pipeline in a more functional approach which removes a lot of the boiler plate code and complexity you get from building classes in larger pipelines as well making it much easier for people to dive into Hot-Monkey-Engine.

## About Hot-Monkey-Engine

Hot-Monkey-Engine is designed to allow a pipeline to web-scraping enforcing scraping logic to be separated from the core application logic. Hot-Monkey-Engine allows integration with date from multiple sites/pages to be handled to return a list of objects which you can use at the other end without the need to merge together.

Hot-Monkey-Engine also tries to tackle pages where certain features are hidden behind JavaScript allowing more data to be accessed. Hot-Monkey-Engine allows even more data to be accessed and allows even more access to automated web-scraping without the need to know which URL endpoints to hit.

Lastly, Hot-Monkey-Engine  tries to tackle the ever changing nature of website UI. Hot-Monkey-Engine designed to be able to identify such changes and allows you to resolve it quickly. Since Hot-Monkey-Engine is designed to be separated from the application logic, this means its much easier to integrate into your application without having it tightly coupled to your application logic.

## Installation

To Install the application,use the following pip command

```bash
pip instal hot-monkey-engine
```

Once installed, you can call it as shown in the example below which will simply count the unique tags sent down:

```python
import hot-monkey-engine as hme

# hme.config()

await hme.request('https://example.com')

unquie_tag_count = hme.scrape_elements() \
    .map(lambda tagname: (tagname, 1)) \
    .reduceBytag(lambda a, b: a + b)

print(unquie_tag_count)
```

## Configuration

There are a few configuration settings available so that you can use what ever browser you want.

### Changing Browsers

By default, when the code runs, it will automatically download ########## browser. It will store this browser in user directory. It will link this path by setting an environment variable of $SCRAPEBROWSER to this location. Though you must accept it in terminal.

You can change this to point to another browser locally as long as you either set the environment path for $SCRAPEBROWSER to the path of your chosen browser (as long as it is compatible with selenium).

You can also change the directory via code as well setting this path in code as seen below. This allows you to be very flexible with the browser you use and making it more shippable to other platforms.

```python
import hot-monkey-engine as hme

hme.config( browser = "/path/to/browser")
```

### JavaScript config

Due to how javascript calls can last for a period of time (or forever), we need to be able to cut it off after a certain period of time. By default, the config setting waits for the onload javascript to be completed before starting the scraping. Note that all of the waits can be cancelled early within the scraping. This can be done only when a certain criterion are met. These config changes allows you to put a default wait method for all calls to this library so that your code doesn't get stuck on a piece of javascript forever (or allowing you to do the opposite).

```python
import hot-monkey-engine as hme
import hot-monkey-engine.javascript as js

hme.config( javascript_wait = js.WaitUntilComplete)
```

But this can be changed so that the javascript is disabled from running allowing te HTML to be scraped entirely

```python
import hot-monkey-engine as hme

hme.config( javascript_enable = False)
```

We can also allow the javascript to run but not wait for it and start parsing straight away.

```python
import hot-monkey-engine as hme
import hot-monkey-engine.javascript as js

hme.config( javascript_wait = js.NeverWait)
```

We can further wait until the javascript until a certain amount of time in milliseconds.

```python
import hot-monkey-engine as hme
import hot-monkey-engine.javascript as js

hme.config( javascript_wait = js.WaitUpToMilliseconds, javascript_wait_time = 1000)
```

### Headless mode config

Hot-Monkey-Engine allows you to open chosen browser in a viewable state so you can see exactly what is going wrong. By enabling these settings at the start, the browser of your choosing will pop up and animate your scraping by highlighting whats been looked at, whats been scrapped and whats been interacted with. Note you should also set a pause per scrape which will slow the scraping down but it will allow you to visibly see what is going on.

```python
import hot-monkey-engine as hme

hme.config( headless_mode = True, animate_scraping = True, pause_per_scrape = 1000)
```

## Examples

### Simple single page scan

### Simple webpage scan

### Wait until javascript loads page

### Multi page scrape

### Detect specific page change scrape

What if we want to scrape the same page on a timer? Luckily, this library as a built in way to detect differences on the page. This will run in a different thread.

```python
import hot-monkey-engine as hme

hme.config()

hme

```

## Troubleshooting

If there is an issues please refer to the QA (URL_HERE), wiki (URL_HERE), or send me an email at EMAIL@EMAIL.EMAIL
