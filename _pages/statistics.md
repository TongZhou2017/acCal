---
layout: default
title: 统计信息
permalink: /statistics/
---

<div class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
  <div class="mb-8">
    <h1 class="text-3xl font-bold text-white mb-2">📊 统计信息</h1>
    <p class="text-gray-400">了解学术会议数据的各个维度统计</p>
  </div>

  <!-- 总体统计卡片 -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    {% assign total_conferences = 0 %}
    {% assign upcoming_conferences = 0 %}
    {% assign open_deadlines = 0 %}
    {% assign closed_deadlines = 0 %}
    {% assign today = "now" | date: "%s" %}
    
    {% for conference in site.conferences %}
      {% unless conference.draft %}
        {% assign total_conferences = total_conferences | plus: 1 %}
        {% assign conf_date = conference.date_start | date: "%s" %}
        {% if conf_date >= today %}
          {% assign upcoming_conferences = upcoming_conferences | plus: 1 %}
        {% endif %}
        {% if conference.deadline != 'N/A' and conference.deadline != '' %}
          {% assign deadline_date = conference.deadline | date: "%s" %}
          {% if deadline_date >= today %}
            {% assign open_deadlines = open_deadlines | plus: 1 %}
          {% else %}
            {% assign closed_deadlines = closed_deadlines | plus: 1 %}
          {% endif %}
        {% endif %}
      {% endunless %}
    {% endfor %}

    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-gray-400 mb-1">总会议数</p>
          <p class="text-3xl font-bold text-white">{{ total_conferences }}</p>
        </div>
        <div class="text-4xl opacity-50">📅</div>
      </div>
    </div>

    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-gray-400 mb-1">即将召开</p>
          <p class="text-3xl font-bold text-brand">{{ upcoming_conferences }}</p>
        </div>
        <div class="text-4xl opacity-50">🚀</div>
      </div>
    </div>

    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-gray-400 mb-1">未截稿</p>
          <p class="text-3xl font-bold text-green-400">{{ open_deadlines }}</p>
        </div>
        <div class="text-4xl opacity-50">✅</div>
      </div>
    </div>

    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm text-gray-400 mb-1">已截稿</p>
          <p class="text-3xl font-bold text-gray-500">{{ closed_deadlines }}</p>
        </div>
        <div class="text-4xl opacity-50">⏰</div>
      </div>
    </div>
  </div>

  <!-- 统计图表区域 -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
    <!-- 学科领域分布 -->
    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <h2 class="text-xl font-bold text-white mb-4">学科领域分布</h2>
      <div style="height: 300px; position: relative;">
        <canvas id="disciplineChart"></canvas>
      </div>
    </div>

    <!-- 月份分布 -->
    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <h2 class="text-xl font-bold text-white mb-4">月份分布</h2>
      <div style="height: 300px; position: relative;">
        <canvas id="monthChart"></canvas>
      </div>
    </div>

    <!-- 省份分布 -->
    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <h2 class="text-xl font-bold text-white mb-4">省份分布</h2>
      <div style="height: 300px; position: relative;">
        <canvas id="provinceChart"></canvas>
      </div>
    </div>

    <!-- 季度分布 -->
    <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
      <h2 class="text-xl font-bold text-white mb-4">季度分布</h2>
      <div style="height: 300px; position: relative;">
        <canvas id="quarterChart"></canvas>
      </div>
    </div>
  </div>

  <!-- 详细统计表格 -->
  <div class="bg-cardbg border border-gray-700 rounded-xl p-6 mb-8">
    <h2 class="text-xl font-bold text-white mb-4">详细统计</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-gray-700">
            <th class="text-left py-3 px-4 text-gray-400 font-semibold">维度</th>
            <th class="text-left py-3 px-4 text-gray-400 font-semibold">统计项</th>
            <th class="text-right py-3 px-4 text-gray-400 font-semibold">数量</th>
            <th class="text-right py-3 px-4 text-gray-400 font-semibold">占比</th>
          </tr>
        </thead>
        <tbody id="statisticsTable">
          <!-- 通过 JavaScript 动态生成 -->
        </tbody>
      </table>
    </div>
  </div>

  <!-- 标签云 -->
  <div class="bg-cardbg border border-gray-700 rounded-xl p-6">
    <h2 class="text-xl font-bold text-white mb-4">热门标签</h2>
    <div id="tagCloud" class="flex flex-wrap gap-2">
      <!-- 通过 JavaScript 动态生成 -->
    </div>
  </div>
</div>

<!-- Chart.js -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<script>
  // 会议数据
  const conferences = [
    {% for conference in site.conferences %}
      {% unless conference.draft %}
        {
          title: {{ conference.title | jsonify }},
          discipline: {{ conference.discipline | jsonify }},
          location: {{ conference.location | jsonify }},
          dateStart: {{ conference.date_start | jsonify }},
          dateEnd: {{ conference.date_end | jsonify }},
          deadline: {{ conference.deadline | jsonify }},
          tags: {{ conference.tags | jsonify }},
        },
      {% endunless %}
    {% endfor %}
  ];

  // 统计函数
  function getDisciplineStats() {
    const stats = {};
    conferences.forEach(conf => {
      const disc = conf.discipline || '其他';
      // 提取学科名称（去除英文）
      let discName = disc.split('(')[0].trim();
      if (discName === '') discName = '其他';
      stats[discName] = (stats[discName] || 0) + 1;
    });
    return stats;
  }

  function getMonthStats() {
    const stats = {};
    const monthNames = ['1月', '2月', '3月', '4月', '5月', '6月', 
                       '7月', '8月', '9月', '10月', '11月', '12月'];
    conferences.forEach(conf => {
      const date = new Date(conf.dateStart);
      const month = date.getMonth();
      const monthName = monthNames[month];
      stats[monthName] = (stats[monthName] || 0) + 1;
    });
    return stats;
  }

  function getProvinceStats() {
    const stats = {};
    conferences.forEach(conf => {
      const location = conf.location || '';
      const province = location.split('-')[0]?.trim() || '未知';
      stats[province] = (stats[province] || 0) + 1;
    });
    return stats;
  }

  function getQuarterStats() {
    const stats = { 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0 };
    conferences.forEach(conf => {
      const date = new Date(conf.dateStart);
      const month = date.getMonth();
      const quarter = Math.floor(month / 3) + 1;
      stats[`Q${quarter}`] = (stats[`Q${quarter}`] || 0) + 1;
    });
    return stats;
  }

  function getTagStats() {
    const stats = {};
    conferences.forEach(conf => {
      if (conf.tags && Array.isArray(conf.tags)) {
        conf.tags.forEach(tag => {
          stats[tag] = (stats[tag] || 0) + 1;
        });
      }
    });
    return stats;
  }

  // 图表配置
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    layout: {
      padding: {
        top: 10,
        bottom: 10,
        left: 10,
        right: 10
      }
    },
    plugins: {
      legend: {
        labels: {
          color: '#9CA3AF'
        }
      }
    },
    scales: {
      y: {
        ticks: {
          color: '#9CA3AF',
          maxTicksLimit: 10
        },
        grid: {
          color: '#374151'
        },
        beginAtZero: true
      },
      x: {
        ticks: {
          color: '#9CA3AF',
          maxTicksLimit: 12
        },
        grid: {
          color: '#374151'
        },
        beginAtZero: true
      }
    }
  };

  // 学科领域分布图表
  const disciplineStats = getDisciplineStats();
  const disciplineData = {
    labels: Object.keys(disciplineStats),
    datasets: [{
      label: '会议数量',
      data: Object.values(disciplineStats),
      backgroundColor: [
        'rgba(16, 185, 129, 0.6)',
        'rgba(59, 130, 246, 0.6)',
        'rgba(245, 158, 11, 0.6)',
        'rgba(236, 72, 153, 0.6)',
        'rgba(139, 92, 246, 0.6)',
        'rgba(239, 68, 68, 0.6)',
      ],
      borderColor: [
        'rgba(16, 185, 129, 1)',
        'rgba(59, 130, 246, 1)',
        'rgba(245, 158, 11, 1)',
        'rgba(236, 72, 153, 1)',
        'rgba(139, 92, 246, 1)',
        'rgba(239, 68, 68, 1)',
      ],
      borderWidth: 2
    }]
  };
  new Chart(document.getElementById('disciplineChart'), {
    type: 'doughnut',
    data: disciplineData,
    options: chartOptions
  });

  // 月份分布图表
  const monthStats = getMonthStats();
  const monthLabels = ['1月', '2月', '3月', '4月', '5月', '6月', 
                       '7月', '8月', '9月', '10月', '11月', '12月'];
  const monthData = {
    labels: monthLabels,
    datasets: [{
      label: '会议数量',
      data: monthLabels.map(m => monthStats[m] || 0),
      backgroundColor: 'rgba(5, 150, 105, 0.6)',
      borderColor: 'rgba(5, 150, 105, 1)',
      borderWidth: 2
    }]
  };
  new Chart(document.getElementById('monthChart'), {
    type: 'bar',
    data: monthData,
    options: chartOptions
  });

  // 省份分布图表
  const provinceStats = getProvinceStats();
  const sortedProvinces = Object.entries(provinceStats)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8); // 只显示前8个，避免图表过长
  const provinceData = {
    labels: sortedProvinces.map(p => p[0]),
    datasets: [{
      label: '会议数量',
      data: sortedProvinces.map(p => p[1]),
      backgroundColor: 'rgba(245, 158, 11, 0.6)',
      borderColor: 'rgba(245, 158, 11, 1)',
      borderWidth: 2
    }]
  };
  new Chart(document.getElementById('provinceChart'), {
    type: 'bar',
    data: provinceData,
    options: {
      ...chartOptions,
      indexAxis: 'y',
      scales: {
        x: {
          ticks: {
            color: '#9CA3AF',
            maxTicksLimit: 8,
            stepSize: 1
          },
          grid: {
            color: '#374151'
          },
          beginAtZero: true
        },
        y: {
          ticks: {
            color: '#9CA3AF'
          },
          grid: {
            color: '#374151'
          }
        }
      }
    }
  });

  // 季度分布图表
  const quarterStats = getQuarterStats();
  const quarterData = {
    labels: ['Q1 (1-3月)', 'Q2 (4-6月)', 'Q3 (7-9月)', 'Q4 (10-12月)'],
    datasets: [{
      label: '会议数量',
      data: [quarterStats.Q1, quarterStats.Q2, quarterStats.Q3, quarterStats.Q4],
      backgroundColor: [
        'rgba(59, 130, 246, 0.6)',
        'rgba(16, 185, 129, 0.6)',
        'rgba(245, 158, 11, 0.6)',
        'rgba(236, 72, 153, 0.6)',
      ],
      borderColor: [
        'rgba(59, 130, 246, 1)',
        'rgba(16, 185, 129, 1)',
        'rgba(245, 158, 11, 1)',
        'rgba(236, 72, 153, 1)',
      ],
      borderWidth: 2
    }]
  };
  new Chart(document.getElementById('quarterChart'), {
    type: 'pie',
    data: quarterData,
    options: chartOptions
  });

  // 生成详细统计表格
  function generateStatisticsTable() {
    const tableBody = document.getElementById('statisticsTable');
    const total = conferences.length;
    
    // 学科统计
    Object.entries(disciplineStats).forEach(([name, count]) => {
      const row = document.createElement('tr');
      row.className = 'border-b border-gray-800 hover:bg-darkbg';
      row.innerHTML = `
        <td class="py-3 px-4 text-gray-300">学科领域</td>
        <td class="py-3 px-4 text-white">${name}</td>
        <td class="py-3 px-4 text-right text-gray-300">${count}</td>
        <td class="py-3 px-4 text-right text-gray-300">${((count / total) * 100).toFixed(1)}%</td>
      `;
      tableBody.appendChild(row);
    });

    // 省份统计（前10）
    sortedProvinces.forEach(([name, count]) => {
      const row = document.createElement('tr');
      row.className = 'border-b border-gray-800 hover:bg-darkbg';
      row.innerHTML = `
        <td class="py-3 px-4 text-gray-300">省份</td>
        <td class="py-3 px-4 text-white">${name}</td>
        <td class="py-3 px-4 text-right text-gray-300">${count}</td>
        <td class="py-3 px-4 text-right text-gray-300">${((count / total) * 100).toFixed(1)}%</td>
      `;
      tableBody.appendChild(row);
    });
  }

  // 生成标签云
  function generateTagCloud() {
    const tagStats = getTagStats();
    const sortedTags = Object.entries(tagStats)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 20); // 显示前20个标签
    
    const maxCount = Math.max(...sortedTags.map(t => t[1]));
    const minCount = Math.min(...sortedTags.map(t => t[1]));
    const sizeRange = 12; // 字体大小范围 (px)
    const minSize = 14;
    
    const tagCloud = document.getElementById('tagCloud');
    sortedTags.forEach(([tag, count]) => {
      // 根据频率计算字体大小
      const size = minSize + (count - minCount) / (maxCount - minCount) * sizeRange;
      // 根据频率计算透明度
      const opacity = 0.6 + (count - minCount) / (maxCount - minCount) * 0.4;
      
      const tagElement = document.createElement('span');
      tagElement.className = 'px-3 py-1 rounded-lg bg-darkbg border border-gray-700 hover:border-brand transition';
      tagElement.style.fontSize = `${size}px`;
      tagElement.style.opacity = opacity;
      tagElement.textContent = `${tag} (${count})`;
      tagCloud.appendChild(tagElement);
    });
  }

  // 初始化
  generateStatisticsTable();
  generateTagCloud();
</script>

