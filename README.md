# pyTun
<h2>Maya Calendar Tools</h2>

This is a Python app for converting between the Maya and Western (Gregorian and Julian) calendars.

<img src="app/static/images/app_screen.png">

<h2>Instructions</h2>

The Classic Maya kept track of historical events using three main calendars. The <b>Long Count</b> represented the number of days ellapsed since the creation of the present Cosmos, which the Maya reckoned to have happened about five thousand years ago. This date was expressed in the vigesimal system, with units of 1, 20, 360, 7,200 and 144,000 days.

Besides the Long Count, the Classic Maya used two other calendars called <b>Tzolk'in</b> and <b>Haab</b> - which, together, form the <b>Calendar Round</b>. Unlike the Long Count, these calendars are cyclical, and a date in the Calendar Round will repeat itself every 52 years. The Tzolk'in is a 260-day cycle where each day has a number between 1 and 13 and a name in a sequence of 20 names. The Haab corresponds to the 365 days of the solar year and is divided into 18 'months' of 20 days, plus an additional month of 5 days.

In order to perform the conversion, we need a <b>correlation constant</b> that anchors a Maya date in the Western calendar. Mayanists employ a Julian Day Number (a system used by astronomers) as a constant. This expresses the number of days ellapsed between the Julian Day Zero (Jan 1 4713 BCE) and the Maya Long Count 0.0.0.0.0. The most common correlation constant used in the literature is 584285, a little correction of Thompson-Goodman-Martinez correlation of 584283.

Maya dates are converted to the <b>Gregorian Calendar</b> and to the <b>Julian Calendar</b>. The Gregorian Calendar was only established in 1582. Before that, dates in the Western World were expressed using the Julian Calendar. Any Gregorian date before 1582 is called 'proleptic', because it is merely a projection. The difference between the two calendars is in the treatment of leap years. In the Gregorian Calendar, extra days are added to years exactly divisible by 400, which otherwise would not be leap years. Because this rule did not exist in the Julian Calendar, a difference of 10 days had accumulated between the Julian year and the actual solar year in 1582 when the Gregorian Calendar was instituted.

<a href="http://mayadate.herokuapp.com/" target="_blank">Go to the app</a>
