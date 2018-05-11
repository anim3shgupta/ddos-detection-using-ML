// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling

function createCharts(msg, selection){
  google.charts.load('current', {'packages':['corechart', 'bar']});
  google.charts.setOnLoadCallback(drawLineChart);
  google.charts.setOnLoadCallback(drawBarChart);
  google.charts.setOnLoadCallback(drawPieChart);

  // ################################################
  // Line Chart
  // ################################################
  function drawLineChart() {
    var chart;
    var data;
    data = new google.visualization.DataTable();
    data.addColumn('number', 'Packet Number');
    data.addColumn('number', 'Class');
    
    for (var i = 0; i < msg.length; i++) { 
      if (msg[i] == 'normal')
        data.addRow([i, 0]);
      else
        data.addRow([i, 1]);   
    }
    
    var options = {
      height: 350,
      legend: { position: 'left' },
      hAxis: {
        title: 'Packet',
        textStyle: {
          bold: true,
          fontSize: 12,
          color: '#848484'
        },
        titleTextStyle: {
          bold: true,
          fontSize: 16,
          color: 'Black',
          italic: false
        }
      },
      vAxis: {
        title: 'Attack?',
        textStyle: {
          fontSize: 14,
          bold: true,
          color: '#848484'
        },
        titleTextStyle: {
          fontSize: 16,
          bold: true,
          color: 'Black',
          italic: false
        }
      }
    };

    chart = new google.visualization.LineChart(document.getElementById('myAreaChart'));
    chart.draw(data, options);
  }

  // ################################################
  // -- Bar Chart
  // ################################################
  function drawBarChart(){
    var data;
    var chart;
    var normalPackets = 0;
    var attackPackets = 0;

    for (var i = 0; i < msg.length; i++) {
      if (msg[i] == 'normal')
        normalPackets = normalPackets + 1;
      else
        attackPackets = attackPackets + 1;
    }

    console.log("The number of attack packets are:")
    console.log(attackPackets)

    data = google.visualization.arrayToDataTable([
        ["Class", "#", { role: "style" }],
        ["Normal", normalPackets, "green"],
        ["Attack", attackPackets, "red"]
      ]);

    var options = {
      width: 800,
      height: 300,
      legend: { position: 'none' },  
      hAxis: {
        title: 'Number of Packets',
        textStyle: {
          bold: true,
          fontSize: 12,
          color: '#848484'
        },
        titleTextStyle: {
          bold: true,
          fontSize: 16,
          color: 'Black',
          italic: false

        }
      },
      vAxis: {
        title: 'Class',
        textStyle: {
          fontSize: 14,
          bold: true,
          color: '#848484'
        },
        titleTextStyle: {
          fontSize: 16,
          bold: true,
          color: 'Black',
          italic: false
        }
      }
    };
    var chart = new google.visualization.BarChart(document.getElementById('myBarChart'));
    chart.draw(data, options);
  }


  // ################################################
  // Pie Chart
  // ################################################
  function drawPieChart(){
    fs = selection['featureAlgorithm']
    clx = selection['classification']
    var tn;
    var fp;
    var fn;
    var tp;

    if(fs == 1 && clx == 1){
      tn = 8945;
      fp = 136;
      fn = 253;
      tp = 15367;
    }

    else if(fs == 1 && clx == 2){
      tn = 0;
      fp = 0;
      fn = 0;
      tp = 0;
    }

    else if(fs == 1 && clx == 3){
      tn = 9039;
      fp = 42;
      fn = 18;
      tp = 15602;
    }

    else if(fs == 1 && clx == 4){
      tn = 9057;
      fp = 24;
      fn = 17;
      tp = 15603;
    }

    else if(fs == 2 && clx == 1){
      tn = 8961;
      fp = 120;
      fn = 436;
      tp = 15184;
    }

    else if(fs == 2 && clx == 2){
      tn = 0;
      fp = 0;
      fn = 0;
      tp = 0;
    }

    else if(fs == 2 && clx == 3){
      tn = 8978;
      fp = 103;
      fn = 27;
      tp = 15593;
    }

    else if(fs == 2 && clx == 4){
      tn = 8991;
      fp = 90;
      fn = 30;
      tp = 15590;
    }

    else if(fs == 3 && clx == 1){
      tn = 15211;
      fp = 409;
      fn = 130;
      tp = 8951;
    }

    else if(fs == 3 && clx == 2){
      tn = 0;
      fp = 0;
      fn = 0;
      tp = 0;
    }

    else if(fs == 3 && clx == 3){
      tn = 15493;
      fp = 127;
      fn = 44;
      tp = 9037;
    }

    else if(fs == 3 && clx == 4){
      tn = 15500;
      fp = 120;
      fn = 35;
      tp = 9046;
    }

    else if(fs == 4 && clx == 1){
      tn = 3672;
      fp = 11948;
      fn = 41;
      tp = 9040;
    }

    else if(fs == 4 && clx == 2){
      tn = 1965;
      fp = 35;
      fn = 0;
      tp = 0;
    }

    else if(fs == 4 && clx == 3){
      tn = 15588;
      fp = 32;
      fn = 18;
      tp = 9063;
    }

    else if(fs == 4 && clx == 4){
      tn = 15607;
      fp = 13;
      fn = 4;
      tp = 9077;
    }


    var data = google.visualization.arrayToDataTable([
          ['Metric', 'Value'],
          ['True Negative', tn],
          ['False Positive', fp],
          ['False Negative', fn],
          ['True Positive', tp]
        ]);

    var options = {
      chartArea:{left:20,top:20,width:'200%',height:'200%'}
    };

    var chart = new google.visualization.PieChart(document.getElementById('myPieChart'));
    chart.draw(data, options);

  }

  }





  // -- Pie Chart Example

