const { chromium, firefox, webkit } = require('playwright');

(async () => {
  for (const browserType of [chromium, firefox, webkit]) {
    const browser = await browserType.launch();
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto("https://amazon.com");
    await page.waitForTimeout(1000);
    await browser.close();
  }
})();
