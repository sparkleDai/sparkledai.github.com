document.write('<script type="text/javascript" src="http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js"></script>')

var Weather = {};

//Member
Weather.searchCityServerUrl_ = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js";

//Function
Weather.loadJS = function (url, bindFunction) {
    var oHead = document.getElementsByTagName('HEAD').item(0);
    var oScript = document.createElement("script");
    oScript.type = "text/javascript";
    oScript.src = url;
    oHead.appendChild(oScript);
    if (bindFunction !== undefined && bindFunction !== null && typeof (bindFunction) === "function") {
        oScript.onload = function () {
            bindFunction();
        };
    }
}

Weather.getWeather = function (showWeatherParentObj, city, futureDays) {//根据city的值获取天气信息
    remote_ip_info = StorageSp.getItem(StorageSp.StorageKeySet.RemoteIpInfo);  
    if (remote_ip_info === undefined
        || remote_ip_info === null
        || remote_ip_info.city === undefined
        || remote_ip_info.city === null) {
        Weather.loadJS(Weather.searchCityServerUrl_,
           function () { return showWeather(); }
          );
    }
    else {
        showWeather();
    }

    function showWeather() {
        StorageSp.setItem(StorageSp.StorageKeySet.RemoteIpInfo, remote_ip_info.toJSONString());  
        if (city === undefined || city === null || city.length <= 0) {
            city = remote_ip_info.city;
        }

        if (futureDays === undefined || futureDays === null) {
            futureDays = 2;
        }

        var weatherServerUrl = "http://php.weather.sina.com.cn/iframe/index/w_cl.php?code=js&day=" + futureDays.toString() + "&city=" + city + "&dfc=3";

        Weather.loadJS(weatherServerUrl,
           function () { return generateWeatherObj(city, futureDays, showWeatherParentObj); }
          );
        function generateWeatherObj(city, futureDays, showWeatherParentObj) {

            weatherKey = { sky: 's1', windPower: 'p1', windDirection: 'd1', temperature: 't1' };
            var weatherOjb = '<table>'
                          + ' <tr> '
                          + '   <th id="city"> '
                          + city.toString()
                          + '  </th> '
                          + '   <th> '
                          + '      今天 '
                          + '  </th> '
                          + '  <th> '
                          + '      明天 '
                          + '  </th> '
                          + ' <th> '
                          + '     后天 '
                          + ' </th> '
                          + '</tr>'
            var skyInfo =
                           '<tr>'
                         + ' <th>'
                         + '    天气'
                         + ' </th> ';
            var temperatureInfo =
                           '<tr>'
                         + ' <th>'
                         + '    温度'
                         + ' </th> ';
            var windDirection =
                           '<tr>'
                         + ' <th>'
                         + '    风向'
                         + ' </th> ';
            var windPower =
                           '<tr>'
                         + ' <th>'
                         + '    风力'
                         + ' </th> ';
            for (var index = 0; index <= futureDays; index++) {
                skyInfo += '<td>' + window.SWther.w[city][index][weatherKey.sky] + '</td>';
                temperatureInfo += '<td>' + window.SWther.w[city][index][weatherKey.temperature] + '</td>';
                windDirection += '<td>' + window.SWther.w[city][index][weatherKey.windDirection] + '</td>';
                windPower += '<td>' + window.SWther.w[city][index][weatherKey.windPower] + '</td>';
            }
            skyInfo += '</tr>';
            temperatureInfo += '</tr>';
            windDirection += '</tr>';
            windPower += '</tr>';

            weatherOjb += skyInfo
                        + temperatureInfo
                        + windDirection
                        + windPower
                        + '</table>';
            if (showWeatherParentObj !== undefined && showWeatherParentObj !== null) {
                showWeatherParentObj.innerHTML = weatherOjb;
            }
        }
    }
}


 