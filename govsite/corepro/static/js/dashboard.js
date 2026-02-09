document.addEventListener("DOMContentLoaded", function () {
  // Vertical Bar Chart
  const ctx1 = document.getElementById("verticalBarChart");
  if (ctx1) {
    new Chart(ctx1, {
      type: "bar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
        ],
        datasets: [
          {
            label: "Title of Vertical Bar Chart",
            data: [12, 19, 3, 5, 2, 21, 3, 4, 1, 9, 4, 11],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Horizontal Bar Chart
  const ctx2 = document.getElementById("horizontalBarChart");
  if (ctx2) {
    new Chart(ctx2, {
      type: "bar", // horizontalBar removed in v4
      data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
          {
            label: "Title of Horizontal Bar Chart",
            data: [-12, 19, 3, -5, 2, 3],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        indexAxis: "y", // makes it horizontal
        responsive: true,
        scales: {
          x: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Percentage change",
              font: {
                size: 16,
              },
            },
          },
          y: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Vertical Group Bar Chart
  const ctx3 = document.getElementById("verticalGroupBarChart");
  if (ctx3) {
    new Chart(ctx3, {
      type: "bar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
        ],
        datasets: [
          {
            label: "#2017",
            data: [12, 19, 3, 5, 2, 21, 3, 4, 1, 9, 4, 11],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
          },
          {
            label: "#2018",
            data: [1, 9, 5, 14, 2, 8, 3, 19, 2, 8, 9, 2],
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
          {
            label: "#2019",
            data: [10, 2, 9, 1, 16, 2, 6, 11, 2, 1, 6, 8],
            backgroundColor: "rgba(255, 206, 86, 0.2)",
            borderColor: "rgba(255, 206, 86, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Production Units (in No.)",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Stacked Bar Chart
  const ctx4 = document.getElementById("stackedBarChart");
  if (ctx4) {
    new Chart(ctx4, {
      type: "bar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Dataset 1",
            data: [-12, 3, 2, -5, 2, 3, 5],
            backgroundColor: "rgba(255,99,132, 1)",
            borderWidth: 1,
          },
          {
            label: "Dataset 2",
            data: [-2, 13, 1, 5, 4, 7, 2],
            backgroundColor: "rgba(54,162,235, 1)",
            borderWidth: 1,
          },
          {
            label: "Dataset 3",
            data: [5, 2, 3, -3, 1, 5, 8],
            backgroundColor: "rgba(75,192,192, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: {
            stacked: true,
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
          y: {
            stacked: true,
            title: {
              display: true,
              text: "No. of Units",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Stacked Group Bar Chart
  const ctx5 = document.getElementById("stackedGroupBarChart");
  if (ctx5) {
    new Chart(ctx5, {
      type: "bar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Dataset 1",
            stack: "Stack 0",
            data: [-12, 3, 2, -5, 2, 3, 5],
            backgroundColor: "rgba(255,99,132, 1)",
            borderWidth: 1,
          },
          {
            label: "Dataset 2",
            stack: "Stack 0",
            data: [-2, 13, 1, 5, 4, 7, 2],
            backgroundColor: "rgba(54,162,235, 1)",
            borderWidth: 1,
          },
          {
            label: "Dataset 3",
            stack: "Stack 1",
            data: [5, 2, 3, -3, 1, 5, 8],
            backgroundColor: "rgba(75,192,192, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: {
            stacked: true,
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
          y: {
            stacked: true,
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of Units",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Basic Line Chart
  const ctx6 = document.getElementById("basicLineChart");
  if (ctx6) {
    new Chart(ctx6, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Linear DS 1",
            data: [12, 19, 3, 5, 2, 21, 3],
            backgroundColor: "rgba(255,99,132, 0.2)",
            borderColor: "rgba(255,99,132, 1)",
            borderWidth: 2,
            fill: false,
            tension: 0.5,
          },
          {
            label: "Linear DS 2",
            data: [2, 9, 13, 1, 12, 4, 8],
            backgroundColor: "rgba(54,162,235, 0.2)",
            borderColor: "rgba(54,162,235, 1)",
            borderWidth: 2,
            fill: false,
            tension: 0.5,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  const ctx6a = document.getElementById("basicLineChart2");
  if (ctx6a) {
    const myChart6a = new Chart(ctx6a, {
      type: "line",
      data: {
        labels: [
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
        ],
        datasets: [
          {
            label: "No. of Students Registered",
            data: [
              65982, 72386, 79875, 82567, 89764, 93567, 102273, 136789, 157823,
            ],
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 2,
            fill: true, // ✅ enable fill under line
            tension: 0.5, // smooth curve
            backgroundColor: function (context) {
              const chart = context.chart;
              const { ctx, chartArea } = chart;
              if (!chartArea) {
                return null; // chart not ready yet
              }
              const gradient = ctx.createLinearGradient(
                0,
                chartArea.top,
                0,
                chartArea.bottom,
              );
              gradient.addColorStop(0, "rgba(54, 162, 235, 0.4)");
              gradient.addColorStop(1, "rgba(54, 162, 235, 0)");
              return gradient;
            },
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            labels: {
              font: {
                size: 14,
              },
            },
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: "Years",
              font: {
                size: 16,
              },
            },
          },
          y: {
            title: {
              display: true,
              text: "No. of Students Registered",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Multiaxis Line Chart
  const ctx7 = document.getElementById("multiaxisLineChart");
  if (ctx7) {
    new Chart(ctx7, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Linear DS 1",
            data: [12, 19, 3, 5, 2, 21, 3],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.2)",
            borderWidth: 2,
            fill: false,
            tension: 0.5,
            yAxisID: "y1",
          },
          {
            label: "Logarithmic DS 2",
            data: [2, 1000, 13, 1, 12, 4, 8],
            borderColor: "rgba(54,162,235,1)",
            backgroundColor: "rgba(54,162,235,0.2)",
            borderWidth: 2,
            fill: false,
            tension: 0.5,
            yAxisID: "y2",
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y1: {
            type: "linear",
            position: "left",
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold in linear scale",
              font: {
                size: 16,
              },
            },
          },
          y2: {
            type: "logarithmic",
            position: "right",
            grid: {
              drawOnChartArea: false,
            },
            title: {
              display: true,
              text: "No. of units sold in log scale",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Stepped Line Chart
  const ctx8 = document.getElementById("steppedLineChart");
  if (ctx8) {
    new Chart(ctx8, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Dataset 1",
            data: [12, 19, 3, 5, 2, 21, 3],
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 2,
            stepped: true,
            fill: false,
          },
          {
            label: "Dataset 2",
            data: [2, 9, 13, 1, 12, 4, 8],
            borderColor: "rgba(54,162,235,1)",
            borderWidth: 2,
            stepped: "middle",
            fill: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Interpolation Line Chart
  const ctx9 = document.getElementById("interpolationLineChart");
  if (ctx9) {
    new Chart(ctx9, {
      type: "line",
      data: {
        labels: ["January", "February", "March", "April", "May"],
        datasets: [
          {
            label: "Dataset 1 (monotone)",
            data: [2, 9, 13, 1, 12],
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 2,
            cubicInterpolationMode: "monotone",
            fill: false,
          },
          {
            label: "Dataset 2 (default)",
            data: [2, 9, 13, 1, 12],
            borderColor: "rgba(54,162,2,1)",
            borderWidth: 2,
            fill: false,
          },
          {
            label: "Dataset 3 (linear)",
            data: [2, 9, 13, 1, 12],
            borderColor: "rgba(54,162,235,1)",
            borderWidth: 2,
            tension: 0,
            fill: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Line Styles Chart
  const ctx10 = document.getElementById("lineStylesChart");
  if (ctx10) {
    new Chart(ctx10, {
      type: "line",
      data: {
        labels: ["January", "February", "March", "April", "May"],
        datasets: [
          {
            label: "Dataset 1 (unfilled)",
            data: [2, 9, 13, 1, 12],
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 2,
            fill: false,
          },
          {
            label: "Dataset 2 (dashed)",
            data: [5, 1, 3, 10, 6],
            borderColor: "rgba(54,162,2,1)",
            borderDash: [5, 5],
            borderWidth: 2,
            fill: false,
          },
          {
            label: "Dataset 3 (filled)",
            data: [1, 14, 6, 7, 4],
            borderColor: "rgba(54,162,235,1)",
            backgroundColor: "rgba(54,162,235,0.2)",
            borderWidth: 2,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Point Circle Line Chart
  const ctx11 = document.getElementById("pointCircleLineChart");
  if (ctx11) {
    new Chart(ctx11, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Point style: Circle",
            data: [2, 9, 5, 1, 7, 2, 5],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.5)",
            borderWidth: 2,
            pointStyle: "circle",
            pointRadius: 10,
            pointHoverRadius: 15,
            showLine: false,
            fill: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Point Triangle Line Chart
  const ctx12 = document.getElementById("pointTriangleLineChart");
  if (ctx12) {
    new Chart(ctx12, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Point style: Triangle",
            data: [1, 3, 2, 5, 2, 9, 0],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.5)",
            pointStyle: "triangle",
            pointRadius: 10,
            pointHoverRadius: 15,
            fill: false,
            showLine: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Point CrossRot Line Chart
  const ctx13 = document.getElementById("pointCrossRotLineChart");
  if (ctx13) {
    new Chart(ctx13, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Point style: Cross",
            data: [1, 3, 2, 5, 2, 9, 0],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.5)",
            pointStyle: "crossRot",
            pointRadius: 10,
            pointHoverRadius: 15,
            fill: false,
            showLine: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Point Line Line Chart
  const ctx14 = document.getElementById("pointLineLineChart");
  if (ctx14) {
    new Chart(ctx14, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Point style: Line",
            data: [1, 3, 2, 5, 2, 9, 0],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.5)",
            pointStyle: "line",
            pointRadius: 10,
            pointHoverRadius: 15,
            fill: false,
            showLine: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Fill False Area Chart
  const ctx15 = document.getElementById("fillFalseAreaChart");
  if (ctx15) {
    new Chart(ctx15, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "Area (fill: false)",
            data: [1, 3, 2, -5, 12, -9, 0, 5],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.5)",
            fill: false,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Profit (in percentage)",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Fill Origin Area Chart
  const ctx16 = document.getElementById("fillOriginAreaChart");
  if (ctx16) {
    new Chart(ctx16, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "Area (fill: origin)",
            data: [1, 3, 2, -5, 12, -9, 0, 5],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.3)",
            fill: "origin",
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Profit (in percentage)",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Fill Start Area Chart
  const ctx17 = document.getElementById("fillStartAreaChart");
  if (ctx17) {
    new Chart(ctx17, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "Area (fill: start)",
            data: [1, 3, 2, -5, 12, -9, 0, 5],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.3)",
            fill: "start",
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Profit (in percentage)",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Fill End Area Chart
  const ctx18 = document.getElementById("fillEndAreaChart");
  if (ctx18) {
    new Chart(ctx18, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "Area (fill: end)",
            data: [1, 3, 2, -5, 12, -9, 0, 5],
            borderColor: "rgba(255,99,132,1)",
            backgroundColor: "rgba(255,99,132,0.3)",
            fill: "end",
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Profit (in percentage)",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Datasets Area Chart
  const ctx19 = document.getElementById("datasetsAreaChart");
  if (ctx19) {
    new Chart(ctx19, {
      type: "line",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "#DS 1",
            data: [110, 130, 120, 90, 120, 190, 123, 159],
            backgroundColor: "rgba(54,162,235,0.2)",
            fill: "-1",
          },
          {
            label: "#DS 2",
            data: [100, 119, 103, 83, 102, 162, 112, 139],
            backgroundColor: "rgba(54,162,235,0.3)",
            fill: "-1",
          },
          {
            label: "#DS 3",
            data: [90, 109, 96, 69, 91, 123, 102, 119],
            backgroundColor: "rgba(54,162,235,0.4)",
            fill: "-1",
          },
          {
            label: "#DS 4",
            data: [80, 99, 76, 59, 87, 103, 97, 109],
            backgroundColor: "rgba(54,162,235,0.5)",
            fill: "-1",
          },
          {
            label: "#DS 5",
            data: [60, 59, 56, 39, 67, 83, 77, 89],
            backgroundColor: "rgba(54,162,235,0.6)",
            fill: "-1",
          },
          {
            label: "#DS 6",
            data: [20, 19, 36, 19, 37, 53, 47, 59],
            backgroundColor: "rgba(54,162,235,0.7)",
            fill: "-1",
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "No. of Units sold",
              font: {
                size: 16,
              },
            },
          },
          x: {
            title: {
              display: true,
              text: "Months",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Radar Area Chart
  const ctx20 = document.getElementById("radarAreaChart");
  if (ctx20) {
    new Chart(ctx20, {
      type: "radar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
        ],
        datasets: [
          {
            label: "#DS 1",
            data: [190, 190, 190, 190, 190, 190, 190, 190],
            backgroundColor: "rgba(54,162,235,0.8)",
            fill: 1,
          },
          {
            label: "#DS 2",
            data: [170, 170, 170, 170, 170, 170, 170, 170],
            backgroundColor: "rgba(255,206,86,0.8)",
            fill: 1,
          },
          {
            label: "#DS 3",
            data: [150, 150, 150, 150, 150, 150, 150, 150],
            backgroundColor: "rgba(75,192,192,0.8)",
            fill: 1,
          },
          {
            label: "#DS 4",
            data: [130, 130, 130, 130, 130, 130, 130, 130],
            backgroundColor: "rgba(153,102,255,0.8)",
            fill: 1,
          },
          {
            label: "#DS 5",
            data: [110, 110, 110, 110, 110, 110, 110, 110],
            backgroundColor: "rgba(255,159,64,0.8)",
            fill: 1,
          },
          {
            label: "#DS 6",
            data: [50, 60, 85, 90, 55, 63, 76, 66],
            backgroundColor: "rgba(255,99,132,0.8)",
            fill: 1,
          },
        ],
      },
    });
  }

  // Scatter Chart
  const ctx21 = document.getElementById("scatterChart");
  if (ctx21) {
    new Chart(ctx21, {
      type: "scatter",
      data: {
        datasets: [
          {
            label: "Dataset 1",
            data: [
              {
                x: 2,
                y: 5,
              },
              {
                x: 5,
                y: 6,
              },
              {
                x: 7,
                y: 1,
              },
              {
                x: 9,
                y: 6,
              },
              {
                x: 11,
                y: 3,
              },
              {
                x: 13,
                y: 12,
              },
              {
                x: 6,
                y: 7,
              },
              {
                x: 3,
                y: 10,
              },
            ],
            backgroundColor: "rgba(54,162,255,0.8)",
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 8,
            fill: "1",
          },
          {
            label: "Dataset 2",
            data: [
              {
                x: 0,
                y: 1,
              },
              {
                x: 3,
                y: 6,
              },
              {
                x: 4,
                y: 17,
              },
              {
                x: 8,
                y: 6,
              },
              {
                x: 11,
                y: 7,
              },
              {
                x: 9,
                y: 2,
              },
              {
                x: 5,
                y: 9,
              },
              {
                x: 2,
                y: 1,
              },
            ],
            backgroundColor: "rgba(255,99,132,0.8)",
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 8,
            fill: "1",
          },
          {
            label: "Dataset 3",
            data: [
              {
                x: 1,
                y: 11,
              },
              {
                x: 2,
                y: 12,
              },
              {
                x: 3,
                y: 0,
              },
              {
                x: 5,
                y: 15,
              },
              {
                x: 7,
                y: 8,
              },
              {
                x: 9,
                y: 19,
              },
              {
                x: 10,
                y: 10,
              },
              {
                x: 13,
                y: 1,
              },
            ],
            backgroundColor: "rgba(69,255,112,0.8)",
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 8,
            fill: "1",
          },
          {
            label: "Dataset 4",
            data: [
              {
                x: 0,
                y: 19,
              },
              {
                x: 3,
                y: 3,
              },
              {
                x: 4,
                y: 12,
              },
              {
                x: 7,
                y: 16,
              },
              {
                x: 8,
                y: 10,
              },
              {
                x: 9,
                y: 18,
              },
              {
                x: 11,
                y: 17,
              },
              {
                x: 12,
                y: 11,
              },
            ],
            backgroundColor: "rgba(255,213,13,0.8)",
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 8,
            fill: "1",
          },
        ],
      },
      options: {
        scales: {
          x: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Data input",
              font: {
                size: 16,
              },
            },
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Data output",
              font: {
                size: 16,
              },
            },
          },
        },
      },
    });
  }

  // Doughnut Chart
  const ctx22 = document.getElementById("doughnutChart");
  if (ctx22) {
    new Chart(ctx22, {
      type: "doughnut",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            data: [40, 4, 36, 19, 53, 67, 59],
            backgroundColor: [
              "rgba(255,99,132,1)",
              "rgba(54,162,235,1)",
              "rgba(75,192,192,1)",
              "rgba(255,205,86,1)",
              "rgba(255,159,64,1)",
              "rgba(255,159,164,1)",
              "rgba(255,99,232,1)",
            ],
          },
        ],
      },
    });
  }

  // Doughnut Chart 2
  const ctx22b = document.getElementById("doughnutChart2");
  if (ctx22b) {
    new Chart(ctx22b, {
      type: "doughnut",
      data: {
        labels: ["Successful candidates", "Unsuccessful candidates"],
        datasets: [
          {
            data: [6, 94],
            backgroundColor: ["rgba(75,192,192,1)", "rgba(255,99,132,1)"],
          },
        ],
      },
    });
  }

  // Pie Chart
  const ctx23 = document.getElementById("pieChart");
  if (ctx23) {
    new Chart(ctx23, {
      type: "pie",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            data: [40, 4, 36, 19, 53, 67, 59],
            backgroundColor: [
              "rgba(255,99,132,1)",
              "rgba(54,162,235,1)",
              "rgba(75,192,192,1)",
              "rgba(255,205,86,1)",
              "rgba(255,159,64,1)",
              "rgba(255,159,164,1)",
              "rgba(255,99,232,1)",
            ],
          },
        ],
      },
    });
  }

  // Polar Area Chart
  const ctx24 = document.getElementById("polarAreaChart");
  if (ctx24) {
    new Chart(ctx24, {
      type: "polarArea",
      data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
          {
            data: [40, 9, 36, 19, 53, 67],
            backgroundColor: [
              "rgba(255,99,132,1)",
              "rgba(54,112,235,1)",
              "rgba(75,192,192,1)",
              "rgba(255,205,86,1)",
              "rgba(255,159,64,1)",
              "rgba(255,159,164,1)",
            ],
          },
        ],
      },
    });
  }

  function generateData() {
    function randomNumber(min, max) {
      return Math.random() * (max - min) + min;
    }

    function randomBar(date, lastClose) {
      const close = randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
      return {
        x: date.valueOf(),
        y: close,
      };
    }

    let date = moment("Jan 01 2017", "MMM DD YYYY");
    let now = moment();
    let data = [];

    while (data.length < 200 && date.isBefore(now)) {
      data.push(
        randomBar(date, data.length > 0 ? data[data.length - 1].y : 30),
      );
      date = date.clone().add(1, "day");
    }
    return data;
  }

  const canvas25 = document.getElementById("financialChart");
  let financialChart;

  if (canvas25) {
    const ctx25 = canvas25.getContext("2d");

    const cfg = {
      type: "line",
      data: {
        datasets: [
          {
            label: "Network Signal Traffic",
            backgroundColor: "rgba(54,162,235,0.3)",
            borderColor: "rgba(54,162,235,1)",
            data: generateData(),
            pointRadius: 0,
            fill: true,
            tension: 0,
            borderWidth: 2,
          },
        ],
      },
      options: {
        responsive: true,
        animation: false,
        scales: {
          x: {
            type: "time",
            time: {
              unit: "day",
            },
            title: {
              display: true,
              text: "Time / Duration",
              font: {
                size: 16,
              },
            },
          },
          y: {
            title: {
              display: true,
              text: "MB / sec",
              font: {
                size: 16,
              },
            },
          },
        },
        plugins: {
          tooltip: {
            mode: "index",
            intersect: false,
            callbacks: {
              label: function (tooltipItem) {
                let label = tooltipItem.dataset.label || "";
                if (label) label += ": ";
                label += parseFloat(tooltipItem.raw.y).toFixed(2);
                return label;
              },
            },
          },
        },
      },
    };

    financialChart = new Chart(ctx25, cfg);

    // Update chart button
    document.getElementById("update").addEventListener("click", function () {
      const type = document.getElementById("type").value;
      financialChart.config.type = type;
      financialChart.data.datasets[0].data = generateData();
      financialChart.update();
    });
  }
});
