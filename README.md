# MiniFix CalDAV for Yandex.\*

-   He solves two problems: <s>duraki</s>
    1. The server session periodically flies, and access to the events of the Workshop (in our case) disappears. Fix this by giving I link to all communutues.
    2. Initially a strange compilation of the CalDAV protocol, I realized [RFC 5545](https://tools.ietf.org/html/rfc5545) that it was not done precisely as need, to put it mildly, so I had to rewrite it.
    3. In standardization encoding include ISO.9070.1991 (from the server I fetched Windows-1251), but, he doesn't have Cyrillic characters, because of that, as I think we have something like this. Then I try to get CalDAV from Airbnb, and they have ISO-8859-1 encoding. Example response from Yandex.gov (joke, but can be a truth):
    ```
    BEGIN:STANDARD
    TZOFFSETFROM:+0300
    TZOFFSETTO:+0400
    TZNAME:MSK
    DTSTART:20110327T020000
    RDATE:20110327T020000
    END:STANDARD
    END:VTIMEZONE
    BEGIN:VEVENT
    DTSTART;VALUE=DATE:20190829
    DTEND;VALUE=DATE:20190831
    SUMMARY:ÐÐ°Ð»Ð¾ ÑÐ°Ð±Ð¾ÑÑ Ð½Ð°Ð´ Ð¿ÑÐ¾ÐµÐºÑÐ¾Ð¼ ÑÐ¿ÑÐ¸Ð½ÑÐ° 4.
    UID:EvHpjt9Jyandex.ru
    SEQUENCE:2
    DTSTAMP:20190813T102259Z
    CREATED:20190703T184752Z
    DESCRIPTION:Ð­ÑÐ¾ Ð½Ðµ Ð´ÐµÐ´Ð»Ð°Ð¹Ð½\, Ð° ÑÐµÐºÐ¾Ð¼ÐµÐ½Ð´Ð°ÑÐ¸Ñ Ðº Ð½Ð°ÑÐ°Ð»Ñ ÑÐ°Ð±Ð¾ÑÑ Ð½Ð°Ð´ Ð¿ÑÐ¾ÐµÐºÑÐ¾Ð¼\, ÑÑÐ¾Ð±Ñ Ð´Ð¾ ÐºÐ¾Ð½ÑÐ° ÑÐ»ÐµÐ´ÑÑÑÐµÐ¹ Ð½ÐµÐ´ÐµÐ»Ð¸ Ð¾Ð½ Ð±ÑÐ» ÑÐ´Ð°Ð½\, Ð¿ÑÐ¾Ð²ÐµÑÐµÐ½ Ð¸ Ð·Ð°ÑÑÐµÐ½\, Ñ ÑÑÐµÑÐ¾Ð¼ Ð²Ð½ÐµÑÐµÐ½Ð¸Ñ Ð¿ÑÐ°Ð²Ð¾Ðº\, ÐµÑÐ»Ð¸ Ð¾Ð½Ð¸ Ð±ÑÐ´ÑÑ.\n
    URL:https://calendar.yandex.ru/event?event_id=1044900218
    LAST-MODIFIED:20190703T185033Z
    END:VEVENT
    END:VCALENDAR
    ```
    When reading [RFC 5545](https://tools.ietf.org/html/rfc5545), I found [RFC 4791](https://tools.ietf.org/html/rfc4791) `[Page 39]` for CalDAV of the 2007 year and language writing in the head tag in the attribute of the XML file. Maybe this can help.

### Special thanks

-   Authors of used libraries
-   Me
