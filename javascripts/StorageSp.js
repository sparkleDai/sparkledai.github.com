var StorageSp = {};

StorageSp.StorageKeySet = {
    RemoteIpInfo: 'RemoteIpInfo'
};

StorageSp.listenKeyValueChange = function (listenEvent) {//在调用setItem()、removeItem()或者clear()导致存储发生改变的时候会触发storage事件，但是如果你设置一个已存在的值，或者在一个空的存储区域调用clear()函数，就不会触发storage事件，这个事件不会冒泡也不可以被阻止。据测试，在改变的页面监听storage事件，有可能会无法监听到。需要在其他页面(如果是同一个页面，需要再打开一页监听)进行监听。
    if (window.addEventListener) {
        window.addEventListener("storage", listenEvent, false);
    } else if (window.attachEvent) {
        window.attachEvent("onstorage", listenEvent);
    }
}

StorageSp.getItem = function (key) {
    var value = null;
    if (window.localStorage) {
        value = localStorage.getItem(key);
    } else {
        alert('This browser does NOT support localStorage');
    }
    return value;
}

StorageSp.setItem = function (key, value) {
    if (window.localStorage) {
        localStorage.setItem(key, value);
    } else {
        alert('This browser does NOT support localStorage');
    }
}

