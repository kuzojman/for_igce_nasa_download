var year_begin = [];

for (var i = 1985; i <= 2022; i++) 
{
    year_begin.push(i);
}

var year_end = [];

for (var i = 1985; i <= 2022; i++) 
{
    year_end.push(i);
}

var month_begin = [];

for (var i = 1; i <= 12; i++) 
{
    month_begin.push(i);
}

var month_end = [];

for (var i = 1; i <= 12; i++) 
{
    month_end.push(i);
}

var day_begin = [];

for (var i = 1; i <= 31; i++) 
{
    day_begin.push(i);
}

var day_end = [];

for (var i = 1; i <= 31; i++) 
{
    day_end.push(i);
}

var longitude_grad = [];

for (var i = 0; i < 360; i++) 
{
    longitude_grad.push(i-180);
}

var latitude_grad = [];

for (var i = 0; i < 180; i++) 
{
    latitude_grad.push(i-90);
}

var longitude_min = [];

for (var i = 0; i < 60; i++) 
{
    longitude_min.push(i);
}

longitude_grad.forEach(op => rec_mode.innerHTML += `<option value="${op}">${op}</option>`);
longitude_min.forEach(op => rec_mode_2.innerHTML += `<option value="${op}">${op}</option>`);

latitude_grad.forEach(op => rec_mode_3.innerHTML += `<option value="${op}">${op}</option>`);
longitude_min.forEach(op => rec_mode_4.innerHTML += `<option value="${op}">${op}</option>`);

year_begin.forEach(op => rec_mode_5.innerHTML += `<option value="${op}">${op}</option>`);
year_end.forEach(op => rec_mode_6.innerHTML += `<option value="${op}">${op}</option>`);

month_begin.forEach(op => rec_mode_7.innerHTML += `<option value="${op}">${op}</option>`);
month_end.forEach(op => rec_mode_8.innerHTML += `<option value="${op}">${op}</option>`);

variab = ['T2M_RANGE', 'TS', 'T2MDEW', 'T2MWET', 'T2M_MAX', 'T2M_MIN', 'T2M', 'QV2M', 'RH2M',
'PRECTOTCORR', 'PS', 'WS10M', 'WS10M_MAX', 'WS10M_MIN', 'WS10M_RANGE', 'WS50M', 'WS50M_MAX',
'WS50M_MIN', 'WS50M_RANGE','ALLSKY_SFC_SW_DNI'];

variab.forEach(op => rec_mode_9.innerHTML += `<option value="${op}">${op}</option>`);
