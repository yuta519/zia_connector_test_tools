# Automation Test tools for Zscaler Internet Access

## What is this?
Have you ever used web proxy tools as system administrator? If you have, you may experience below:

- Web proxy unexpectedly blocks Marketing tools, Web Search, ...
- Web proxy allows the site I wanted to block.

It is usual that you try to deploy web proxy tools in your company.
So I developed this tool.

I have deployed a lot of security devices to Japanese companies for over 5 years. From those experiences, I developed this test tool. This tool checks your setting work correct. For example, when you set block an advertisement category, need test if proxy blocks these. But it is difficult to test all settings. So this tool accesses web sites of all categories. And this checks whether proxy allow or block you expected.

At first, this tool support Zscaler Internet Access which is most famous cloud web proxy.


## What is Zscaler?
![Zsclaer Internet Access Architecuture](https://my.kddi.com/files/topics/1206_ext_12_8.jpg)

Zscaler serves a lot of securities as a cloud. Zscaler Internet Access is one of those. This is a cloud security gateway security service and replaces on-premise web proxy.


## Using stacks
- Python
- Selenium (ChromeDriver)


## Reference
- Download Chromedriver
  - [Download page](https://chromedriver.chromium.org/downloads)
- Zscaler Internet Access URL Category
  - [Help page](https://help.zscaler.com/zia/about-url-categories)
