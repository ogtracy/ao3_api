Debugging Issues

1. I had an error like this: "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?"
What do I do?

A: Add this to the top of your code "import lxml" and make sure that lxml is installed 