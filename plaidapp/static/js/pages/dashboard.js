$(document).ready(function() {
    
    "use strict";

    var ctx = document.getElementById('visitorsChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications', 'Applications'],
            datasets: [{
                
                label: 'Approved',
                data: [3, 6, 4, 5, 6, 5, 3, 5, 6, 5, 4],
                backgroundColor: '#5780F7'
            }, {
                label: 'Declined',
                data: [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2],
                backgroundColor: '#b1b1b1'
            }]
        },
        options: {
            responsive: true,
            legend: {
                display: 0 // place legend on the right side of chart
            },
            scales: {
                yAxes: [{
                    display: 0,
                    stacked: true,
                    ticks: {
                        display: 0
                    },
                    gridLines: {
                        color: "rgba(255,255,255,0)"
                    }
                }],
                xAxes: [{
                    display: 0,
                    stacked: true,
                    ticks: {
                        display: 0
                    },
                    gridLines: {
                        color: "rgba(255,255,255,0)"
                    }
                }]
            }
        }
    });
    
    var options = {
            chart: {
                height: 350,
                type: 'bar',
                
    toolbar: {
      show: false
    }
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'	
                },
            },
        
        colors:['#5780F7', '#ffcd36', '#f83a3a'],

            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            series: [{

                name: 'Outstanding Credit ($M)',
                data: [76, 85, 100, 98, 87, 105, 91, 114, 94, 89, 95]
            }, {
                name: 'Total Payment ($M)',
                data: [44, 44, 64, 72, 42, 60, 39, 60, 53, 50, 60]
            }, {
                name: 'Total Delinquent ($M)',
                data: [32, 41, 36, 26, 45, 45, 52, 54, 41, 39, 35]
            }],
            xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
            },
            fill: {
                opacity: 1

            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ ." + val + " Million"
                    }
                }
            }
        }
    var chart = new ApexCharts(
        document.querySelector("#apex1"),
        options
    );

    chart.render();
    
});