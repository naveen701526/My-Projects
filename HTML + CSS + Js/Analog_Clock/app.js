setInterval( () =>
{
    d=new Date();
    htime=d.getHours();
    mtime=d.getMinutes();
    stime=d.getSeconds();
    hrotation=30*htime+mtime/2+stime/120;
    mrotation=6*mtime+stime/10;
    srotation=6*stime;



    document.querySelector( '.hour' ).style.transform=`rotate(${ hrotation }deg)`;
    document.querySelector( '.minutes' ).style.transform=`rotate(${ mrotation }deg)`;
    document.querySelector( '.seconds' ).style.transform=`rotate(${ srotation }deg)`;
}, 1000 );