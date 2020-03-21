<h1>FIFA WEB SCRAPPING SCRIPT</h1>
simple app to trace the price of a FIFA FUT player and sent a notification via e-mail when price is below the target price.
<br><br>

how to run...
<h2>Arguments:</h2>

<ol>
  <li>url of player (futwiz) </li>
  <li>target price to send mail</li>
  <li>google username (without @...)</li>
  <li>password</li>
  <li>addressee (mail to ...)</li>
</ol>

<p>The script will check in an eternal loop until the price is lower than the target price (the frecuency is hardcoded to 30 min, but can be easilly changed)</p>
