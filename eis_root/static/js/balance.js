(function($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });
})(jQuery);

/*chart*/
var data = [{
  id: '0.0',
  parent: '',
  name: 'Завод'
}, {
  id: '1.1',
  parent: '0.0',
  value: 10,
  name: 'Цех1'
}, {
  id: '1.2',
  parent: '0.0',
  value: 5,
  name: 'Цех2'
}, {
  id: '1.3',
  parent: '0.0',
  value: 6,
  name: 'Цех3'
}, {
  id: '1.4',
  parent: '0.0',
  value: 3,
  name: 'Цех4'
}, 

/*1.1*/
{
  id: '2.1',
  parent: '1.1',
  value: 11,
  name: 'Электр энергия'
},
{
  id: '2.2',
  parent: '1.1',
  value: 3,
  name: 'Электр энергияси (ҚТЭМ)'
},
{
  id: '2.3',
  parent: '1.1',
  value: 6,
  name: 'Иссиқлик энергияси'
},
{
  id: '2.4',
  parent: '1.1',
  value: 6,
  name: 'Иссиқлик энергияси (ҚТЭМ)'
},
{
  id: '2.5',
  parent: '1.1',
  value: 7,
  name: 'Табиий газ'
},
{
  id: '2.6',
  parent: '1.1',
  value: 4,
  name: 'Кўмир'
},
{
  id: '2.7',
  parent: '1.1',
  value: 4,
  name: 'Брикет ва ярим брикетлар'
},
{
  id: '2.8',
  parent: '1.1',
  value: 5,
  name: 'Бензин'
},
{
  id: '2.9',
  parent: '1.1',
  value: 5,
  name: 'Дизел ёқилғиси'
},
{
  id: '2.10',
  parent: '1.1',
  value: 5,
  name: 'Мазут'
},
{
  id: '2.11',
  parent: '1.1',
  value: 5,
  name: 'Нефт маҳсулотларининг бошқа турлари'
},
/* 1.2*/
{
  id: '2.12',
  parent: '1.2',
  value: 11,
  name: 'Электр энергия'
},
{
  id: '2.13',
  parent: '1.2',
  value: 3,
  name: 'Электр энергияси (ҚТЭМ)'
},
{
  id: '2.14',
  parent: '1.2',
  value: 6,
  name: 'Иссиқлик энергияси'
},
{
  id: '2.15',
  parent: '1.2',
  value: 6,
  name: 'Иссиқлик энергияси (ҚТЭМ)'
},
{
  id: '2.16',
  parent: '1.2',
  value: 7,
  name: 'Табиий газ'
},
{
  id: '2.17',
  parent: '1.2',
  value: 4,
  name: 'Кўмир'
},
{
  id: '2.18',
  parent: '1.2',
  value: 4,
  name: 'Брикет ва ярим брикетлар'
},
{
  id: '2.19',
  parent: '1.2',
  value: 5,
  name: 'Бензин'
},
{
  id: '2.20',
  parent: '1.2',
  value: 5,
  name: 'Дизел ёқилғиси'
},
{
  id: '2.21',
  parent: '1.2',
  value: 5,
  name: 'Мазут'
},
{
  id: '2.22',
  parent: '1.2',
  value: 5,
  name: 'Нефт маҳсулотларининг бошқа турлари'
},
/*1.3*/
{
  id: '2.23',
  parent: '1.3',
  value: 11,
  name: 'Электр энергия'
},
{
  id: '2.24',
  parent: '1.3',
  value: 3,
  name: 'Электр энергияси (ҚТЭМ)'
},
{
  id: '2.25',
  parent: '1.3',
  value: 6,
  name: 'Иссиқлик энергияси'
},
{
  id: '2.26',
  parent: '1.3',
  value: 6,
  name: 'Иссиқлик энергияси (ҚТЭМ)'
},
{
  id: '2.27',
  parent: '1.3',
  value: 7,
  name: 'Табиий газ'
},
{
  id: '2.28',
  parent: '1.3',
  value: 4,
  name: 'Кўмир'
},
{
  id: '2.29',
  parent: '1.3',
  value: 4,
  name: 'Брикет ва ярим брикетлар'
},
{
  id: '2.30',
  parent: '1.3',
  value: 5,
  name: 'Бензин'
},
{
  id: '2.31',
  parent: '1.3',
  value: 5,
  name: 'Дизел ёқилғиси'
},
{
  id: '2.32',
  parent: '1.3',
  value: 5,
  name: 'Мазут'
},
{
  id: '2.33',
  parent: '1.3',
  value: 5,
  name: 'Нефт маҳсулотларининг бошқа турлари'
},

/* 1.4*/
{
  id: '2.34',
  parent: '1.4',
  value: 11,
  name: 'Электр энергия'
},
{
  id: '2.35',
  parent: '1.4',
  value: 3,
  name: 'Электр энергияси (ҚТЭМ)'
},
{
  id: '2.36',
  parent: '1.4',
  value: 6,
  name: 'Иссиқлик энергияси'
},
{
  id: '2.37',
  parent: '1.4',
  value: 6,
  name: 'Иссиқлик энергияси (ҚТЭМ)'
},
{
  id: '2.38',
  parent: '1.4',
  value: 7,
  name: 'Табиий газ'
},
{
  id: '2.39',
  parent: '1.4',
  value: 4,
  name: 'Кўмир'
},
{
  id: '2.40',
  parent: '1.4',
  value: 4,
  name: 'Брикет ва ярим брикетлар'
},
{
  id: '2.41',
  parent: '1.4',
  value: 5,
  name: 'Бензин'
},
{
  id: '2.42',
  parent: '1.4',
  value: 5,
  name: 'Дизел ёқилғиси'
},

/*Узатилган энергия*/
{
  id: '3.1',
  parent: '2.1',
  value: 11,
  name: 'Технологик'
},
{
  id: '3.2',
  parent: '2.1',
  value: 6,
  name: 'Вентиляция'
},

{
  id: '3.1',
  parent: '2.1',
  value: 11,
  name: 'Ёритиш'
},
{
  id: '3.2',
  parent: '2.1',
  value: 6,
  name: 'Хусусий'
},

{
  id: '3.1',
  parent: '2.12',
  value: 11,
  name: 'Технологик'
},
{
  id: '3.2',
  parent: '2.12',
  value: 6,
  name: 'Вентиляция'
},

{
  id: '3.1',
  parent: '2.12',
  value: 11,
  name: 'Ёритиш'
},
{
  id: '3.2',
  parent: '2.12',
  value: 6,
  name: 'Хусусий'
},

{
  id: '3.1',
  parent: '2.23',
  value: 11,
  name: 'Технологик'
},
{
  id: '3.2',
  parent: '2.23',
  value: 6,
  name: 'Вентиляция'
},

{
  id: '3.1',
  parent: '2.23',
  value: 11,
  name: 'Ёритиш'
},
{
  id: '3.2',
  parent: '2.23',
  value: 6,
  name: 'Хусусий'
},

{
  id: '3.1',
  parent: '2.34',
  value: 11,
  name: 'Технологик'
},
{
  id: '3.2',
  parent: '2.34',
  value: 6,
  name: 'Вентиляция'
},

{
  id: '3.1',
  parent: '2.34',
  value: 11,
  name: 'Ёритиш'
},
{
  id: '3.2',
  parent: '2.34',
  value: 6,
  name: 'Хусусий'
},

];
Highcharts.chart('container', {

  chart: {
    height: '100%'
  },

  // Let the center circle be transparent
  colors: ['transparent'].concat(Highcharts.getOptions().colors),

  title: {
    text: 'Энергия баланси'
  },

  subtitle: {
    text: 'Йиллик <a href="#">.</a>'
  },

  series: [{
    type: 'sunburst',
    data: data,
    allowDrillToNode: true,
    cursor: 'pointer',
    dataLabels: {
      format: '{point.name}',
      filter: {
        property: 'innerArcLength',
        operator: '>',
        value: 16
      },
      rotationMode: 'circular'
    },
    levels: [{
      level: 1,
      levelIsConstant: false,
      dataLabels: {
        filter: {
          property: 'outerArcLength',
          operator: '>',
          value: 64
        }
      }
    }, {
      level: 2,
      colorByPoint: true
    },
    {
      level: 3,
      colorVariation: {
        key: 'brightness',
        to: -0.5
      }
    }, {
      level: 4,
      colorVariation: {
        key: 'brightness',
        to: 0.5
      }
    }]

  }],

  tooltip: {
    headerFormat: '',
    pointFormat: '<b>{point.name}</b> - <b>{point.value}</b>'
  }
});