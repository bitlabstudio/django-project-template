if((function() {
    var t,u,i,j,
        css='textShadow,boxShadow,borderRadius,opacity'.split(','),
        prefixes=',webkit,moz,o,ms,khtml'.split(','),
        nPrefixes=prefixes.length,
        el=document.createElement('i').style;
    styles:for(i=0;t=css[i];i++) {
        t=t.charAt(0).toUpperCase()+t.substr(1);
        for(j=0;j<nPrefixes;j++) {
            u=prefixes[j]+t;
            if(el[u.charAt(0).toLowerCase()+u.substr(1)]!==undefined) continue styles;
        }
        return true;
    }
    return false;
})()) {
    document.getElementById('warning-old-browser').removeAttribute('style');
}

$(document).ready(function() {
    // Warning handling
    $('#warning-old-browser span').css('cursor', 'pointer').click(function() {
        var data = [
            {name: 'csrfmiddlewaretoken', value: getCookie('csrftoken')}
            ,{name: 'session_name', value: 'hide_warning'}
            ,{name: 'session_value', value: true}
        ];
        $.post($(this).attr('data-url'), data, function(data) {
            if (data == 'done') $('#warning-old-browser').remove();
        });
    });
});