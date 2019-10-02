# Hot-Monkey-Engine
Python webscraping framework that revoles around handling javascript scraping alongside HTML scraping. This wraps around the selium driver to give an easier to use framework for webscraping.

# About this framework
This framework is designed to allow a pipeline to webscraping enforcing scraping logic to be seperated from the core application logic. This allows intergration with date from multiple sites/pages to be handled to return a list of objects which you can use at the other end without the need to merge together.

This framework also tries to tackle pages where certain features are hidden behind javascript allowing more data to be accessed. This allows even more data to be accessed and allows even more access to automated webscraping without the need to know which URL endpoints to hit.

Lastly, this framework tries to tackle the ever changing nature of website UI. This framework is designed to be able to identify such changes and allows you to resolve it quickly. Since this framework is designed to be seperated from the application logic, this means that 
