
  // Replace with your dynamic data from Flask if needed
  const topCuisines = { { top_cuisines | safe }};
  const cuisineLabels = Object.keys(topCuisines);
  const cuisineCounts = Object.values(topCuisines);

  const tableBookingData = {{ table_booking_status | safe }};
  const tableLabels = Object.keys(tableBookingData);
  const tableCounts = Object.values(tableBookingData);

  // Bar Chart for Top Cuisines
  const ctxBar = document.getElementById('cuisineBarChart').getContext('2d');
  new Chart(ctxBar, {
    type: 'bar',
    data: {
      labels: cuisineLabels,
      datasets: [{
        label: 'Count',
        data: cuisineCounts,
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Top 10 Cuisines in Dataset'
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  // Pie Chart for Table Booking
  const ctxPie = document.getElementById('tableBookingPie').getContext('2d');
  new Chart(ctxPie, {
    type: 'pie',
    data: {
      labels: tableLabels,
      datasets: [{
        data: tableCounts,
        backgroundColor: ['#198754', '#dc3545']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Table Booking Distribution'
        }
      }
    }
  });
