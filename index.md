---
layout: default
title: 首页
---

<div class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8 flex flex-col md:flex-row gap-8">
  
  <aside class="w-full md:w-64 flex-shrink-0">
    <div class="bg-cardbg rounded-xl p-5 border border-gray-700 sticky top-24">
      <h3 class="font-bold text-gray-200 mb-4 flex items-center gap-2">
        <svg class="w-5 h-5 text-brand" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path></svg>
        筛选会议
      </h3>
      
      <div class="space-y-6">
        <div>
          <div class="flex items-center justify-between mb-3">
            <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider">学科领域</p>
            <div class="flex gap-2">
              <label class="flex items-center gap-1 cursor-pointer">
                <input type="checkbox" id="select-all-disciplines" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="handleSelectAllDisciplines()">
                <span class="text-xs text-gray-400">全选</span>
              </label>
              <label class="flex items-center gap-1 cursor-pointer">
                <input type="checkbox" id="clear-all-disciplines" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="handleClearAllDisciplines()">
                <span class="text-xs text-gray-400">清除</span>
              </label>
            </div>
          </div>
          <div class="space-y-2">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="life" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">🌿 生命科学</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="earth" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">🌍 地球与环境</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="it" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">💻 信息与工程</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="physical" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">⚛️ 数理化</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="social" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">📚 人文社科</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="medicine" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">🏥 医学与健康</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="other" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand discipline-filter" onchange="handleDisciplineChange()">
              <span class="text-sm">🔬 其他</span>
            </label>
          </div>
        </div>

        <div>
          <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">细分标签</p>
          <div id="tags-filter-container" class="space-y-2 max-h-64 overflow-y-auto">
            <!-- 标签选项将通过 JavaScript 动态生成 -->
          </div>
        </div>

        <div>
          <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">状态</p>
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" id="only-open" class="form-checkbox text-brand rounded bg-darkbg border-gray-600" onchange="filterEvents()">
            <span class="text-sm">仅显示未开始</span>
          </label>
        </div>

        <div>
          <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">时间范围</p>
          <div class="space-y-2">
            <div>
              <label class="block text-xs text-gray-400 mb-1">开始日期</label>
              <input type="date" id="date-start-filter" class="w-full bg-darkbg border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none focus:border-brand focus:ring-1 focus:ring-brand" onchange="filterEvents()">
            </div>
            <div>
              <label class="block text-xs text-gray-400 mb-1">结束日期</label>
              <input type="date" id="date-end-filter" class="w-full bg-darkbg border border-gray-600 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none focus:border-brand focus:ring-1 focus:ring-brand" onchange="filterEvents()">
            </div>
          </div>
        </div>

        <div>
          <button onclick="resetFilters()" class="w-full py-2 bg-brand/10 text-brand text-xs font-bold rounded hover:bg-brand/20 transition">重置筛选</button>
        </div>
      </div>
    </div>
  </aside>

  <section class="flex-1">
    <div class="flex justify-between items-end mb-6">
      <div>
        <h2 class="text-2xl font-bold text-white">即将召开的会议</h2>
      </div>
      <div class="flex gap-2">
        <button id="list-view-btn" onclick="switchView('list')" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 transition">列表视图</button>
        <button id="calendar-view-btn" onclick="switchView('calendar')" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 text-gray-500 transition">日历视图</button>
        <button id="map-view-btn" onclick="switchView('map')" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 text-gray-500 transition">地图视图</button>
        <a href="{{ '/statistics/' | relative_url }}" id="statistics-view-btn" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 text-gray-500 transition">统计视图</a>
      </div>
    </div>

    <div id="list-view" class="space-y-4">
      {% assign conferences = site.conferences | sort: 'date_start' %}
      {% assign count = 0 %}
      {% for conference in conferences %}
        {% unless conference.draft %}
          {% assign count = count | plus: 1 %}
          {% assign date_obj = conference.date_start | date: "%Y-%m-%d" %}
          {% assign month = conference.date_start | date: "%b" | upcase %}
          {% assign day = conference.date_start | date: "%d" | plus: 0 %}
          
          {% assign type_class = "tag-other" %}
          {% assign type_value = "other" %}
          {% if conference.discipline contains "生命科学" or conference.discipline contains "Life Sciences" %}
            {% assign type_class = "tag-life" %}
            {% assign type_value = "life" %}
          {% elsif conference.discipline contains "地球与环境" or conference.discipline contains "Earth & Environment" %}
            {% assign type_class = "tag-earth" %}
            {% assign type_value = "earth" %}
          {% elsif conference.discipline contains "信息与工程" or conference.discipline contains "IT & Engineering" %}
            {% assign type_class = "tag-it" %}
            {% assign type_value = "it" %}
          {% elsif conference.discipline contains "数理化" or conference.discipline contains "Physical Sciences" %}
            {% assign type_class = "tag-physical" %}
            {% assign type_value = "physical" %}
          {% elsif conference.discipline contains "人文社科" or conference.discipline contains "Social Sciences" %}
            {% assign type_class = "tag-social" %}
            {% assign type_value = "social" %}
          {% elsif conference.discipline contains "医学与健康" or conference.discipline contains "Medicine" %}
            {% assign type_class = "tag-medicine" %}
            {% assign type_value = "medicine" %}
          {% endif %}

          {% assign deadline_passed = false %}
          {% if conference.deadline != 'N/A' and conference.deadline != '' %}
            {% assign deadline_date = conference.deadline | date: "%s" %}
            {% assign today = "now" | date: "%s" %}
            {% if deadline_date < today %}
              {% assign deadline_passed = true %}
            {% endif %}
          {% endif %}

          <div class="conference-card bg-cardbg border border-gray-700 rounded-xl p-5 hover:border-brand/50 transition cursor-pointer group relative overflow-hidden" 
               data-type="{{ type_value }}"
               data-date-start="{{ conference.date_start }}"
               data-date-end="{{ conference.date_end }}"
               onclick="window.location.href='{{ conference.url | relative_url }}'">
            <div class="flex gap-4">
              <div class="flex-shrink-0 flex flex-col items-center justify-center bg-darkbg w-16 h-16 rounded-lg border border-gray-700 group-hover:border-brand group-hover:text-brand transition">
                <span class="text-xs font-bold uppercase tracking-wider text-gray-500 group-hover:text-brand/70">{{ month }}</span>
                <span class="text-2xl font-bold text-white group-hover:text-brand">{{ day }}</span>
              </div>
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-1 flex-wrap">
                  {% if conference.tags.size > 0 %}
                    {% for tag in conference.tags limit: 2 %}
                      <span class="text-xs px-2 py-0.5 rounded {{ type_class }}">{{ tag }}</span>
                    {% endfor %}
                  {% else %}
                    <span class="text-xs px-2 py-0.5 rounded {{ type_class }}">{{ conference.discipline }}</span>
                  {% endif %}
                </div>
                <h3 class="text-lg font-bold text-white group-hover:text-brand transition mb-1">
                  <a href="{{ conference.url | relative_url }}" class="hover:text-brand">{{ conference.title }}</a>
                </h3>
                <div class="flex items-center gap-4 text-sm text-gray-400 flex-wrap">
                  <span class="flex items-center gap-1">📍 {{ conference.location }}</span>
                  {% if conference.deadline != 'N/A' and conference.deadline != '' %}
                    <span class="flex items-center gap-1 {% if deadline_passed %}text-gray-600{% else %}text-orange-400{% endif %}">
                      ⚠️ 截稿: {{ conference.deadline }}
                    </span>
                  {% endif %}
                </div>
              </div>
              <div class="hidden sm:flex items-center justify-center">
                <span class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center text-gray-300 group-hover:bg-brand group-hover:text-white transition">➝</span>
              </div>
            </div>
          </div>
        {% endunless %}
      {% endfor %}
      
      {% if count == 0 %}
        <div class="bg-cardbg border border-gray-700 rounded-xl p-8 text-center">
          <p class="text-gray-400 mb-4">暂无会议信息</p>
          <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission.yml" 
             target="_blank" 
             class="inline-block bg-brand hover:bg-brand-light text-white px-6 py-2 rounded-lg font-medium transition">
            提交第一个会议
          </a>
        </div>
      {% endif %}
    </div>

    <div id="calendar-view" class="hidden">
      <div id="calendar-container" class="space-y-8">
        <!-- 日历视图将通过 JavaScript 动态生成 -->
      </div>
    </div>

    <div id="map-view" class="hidden">
      <div id="map-container" class="bg-cardbg border border-gray-700 rounded-xl overflow-hidden" style="height: 600px;">
        <!-- 地图将通过 JavaScript 动态生成 -->
        <div class="flex items-center justify-center h-full text-gray-400">
          <div class="text-center">
            <div class="mb-2">🗺️</div>
            <div>正在加载地图...</div>
          </div>
        </div>
      </div>
      <div class="mt-4 text-sm text-gray-400">
        <p>📍 地图使用高德地图（审图号：GS(2023)2650号）</p>
      </div>
    </div>
    
    <div id="view-footer" class="mt-8 text-center">
      <p class="text-gray-500 text-sm">-- 到底了，去 <a href="https://github.com/{{ site.social.github }}" target="_blank" class="text-brand hover:underline">GitHub</a> 提交更多信息吧 --</p>
    </div>
  </section>
</div>

<!-- 会议数据（隐藏，供 JavaScript 使用） -->
<script id="conferences-data" type="application/json">
[
  {% assign first = true %}
  {% for conference in site.conferences %}
    {% unless conference.draft %}
      {% assign type_value = "other" %}
      {% if conference.discipline contains "生命科学" or conference.discipline contains "Life Sciences" %}
        {% assign type_value = "life" %}
      {% elsif conference.discipline contains "地球与环境" or conference.discipline contains "Earth & Environment" %}
        {% assign type_value = "earth" %}
      {% elsif conference.discipline contains "信息与工程" or conference.discipline contains "IT & Engineering" %}
        {% assign type_value = "it" %}
      {% elsif conference.discipline contains "数理化" or conference.discipline contains "Physical Sciences" %}
        {% assign type_value = "physical" %}
      {% elsif conference.discipline contains "人文社科" or conference.discipline contains "Social Sciences" %}
        {% assign type_value = "social" %}
      {% elsif conference.discipline contains "医学与健康" or conference.discipline contains "Medicine" %}
        {% assign type_value = "medicine" %}
      {% endif %}
      {% unless first %},{% endunless %}{% assign first = false %}
      {
        "id": {{ conference.name | jsonify }},
        "title": {{ conference.title | jsonify }},
        "location": {{ conference.location | jsonify }},
        "dateStart": {{ conference.date_start | jsonify }},
        "dateEnd": {{ conference.date_end | jsonify }},
        "deadline": {{ conference.deadline | jsonify }},
        "type": {{ type_value | jsonify }},
        "url": {{ conference.url | relative_url | jsonify }},
        "tags": {{ conference.tags | jsonify }},
        "discipline": {{ conference.discipline | jsonify }}
      }
    {% endunless %}
  {% endfor %}
]
</script>

<div id="detailModal" class="fixed inset-0 bg-black/80 hidden items-center justify-center z-[100] backdrop-blur-sm" onclick="closeModal('detailModal')">
  <div class="bg-cardbg w-full max-w-2xl rounded-2xl border border-gray-700 shadow-2xl overflow-hidden transform transition-all scale-95" onclick="event.stopPropagation()">
    <div class="h-32 bg-gradient-to-r from-brand-dark to-brand relative">
      <button onclick="closeModal('detailModal')" class="absolute top-4 right-4 bg-black/20 hover:bg-black/40 text-white rounded-full p-1">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
      <div class="absolute bottom-4 left-6">
        <span id="modal-tag" class="px-2 py-0.5 rounded text-xs font-bold bg-white/20 text-white border border-white/20 backdrop-blur-md">TAG</span>
      </div>
    </div>
    <div class="p-6 md:p-8">
      <div class="flex justify-between items-start">
        <h2 id="modal-title" class="text-2xl font-bold text-white mb-2">会议标题</h2>
        <div class="text-center bg-gray-800 rounded px-3 py-1 border border-gray-700">
          <div id="modal-month" class="text-xs text-gray-400 uppercase">DEC</div>
          <div id="modal-day" class="text-xl font-bold text-white">10</div>
        </div>
      </div>
      
      <div class="space-y-4 mt-4">
        <div class="flex items-center gap-3 text-gray-300">
          <span class="w-5 text-center">📍</span>
          <span id="modal-location">地点信息</span>
        </div>
        <div class="flex items-center gap-3 text-gray-300">
          <span class="w-5 text-center">🕒</span>
          <span id="modal-date">时间范围</span>
        </div>
        <div class="flex items-center gap-3 text-brand">
          <span class="w-5 text-center">⚠️</span>
          <span id="modal-deadline">截稿日期</span>
        </div>
      </div>

      <div class="mt-8 pt-6 border-t border-gray-700 flex gap-4">
        <a href="#" id="modal-url" target="_blank" class="flex-1 bg-brand hover:bg-brand-light text-white text-center py-2.5 rounded-lg font-medium transition shadow-lg shadow-brand/20">
          访问官方网站
        </a>
        <button class="px-4 py-2.5 border border-gray-600 rounded-lg hover:bg-gray-700 text-gray-300 transition">
          添加到日历
        </button>
      </div>
    </div>
  </div>
</div>

<script>
  // 获取会议数据
  const conferencesDataScript = document.getElementById('conferences-data');
  const conferencesData = conferencesDataScript ? JSON.parse(conferencesDataScript.textContent) : [];

  // 当前视图状态
  let currentView = 'list';
  let mapInstance = null;
  let mapMarkers = [];
  
  // 高德地图API密钥（从Jekyll配置中获取）
  const AMAP_KEY = '{{ site.amap_key }}' || '';
  
  // 页面加载时初始化
  document.addEventListener('DOMContentLoaded', function() {
    // 初始化全选框状态
    updateSelectAllCheckbox();
    // 初始化标签过滤
    initTagsFilter();
  });

  // 视图切换
  function switchView(view) {
    currentView = view;
    const listView = document.getElementById('list-view');
    const calendarView = document.getElementById('calendar-view');
    const mapView = document.getElementById('map-view');
    const viewFooter = document.getElementById('view-footer');
    const listBtn = document.getElementById('list-view-btn');
    const calendarBtn = document.getElementById('calendar-view-btn');
    const mapBtn = document.getElementById('map-view-btn');

    // 隐藏所有视图
    listView.classList.add('hidden');
    calendarView.classList.add('hidden');
    mapView.classList.add('hidden');
    
    // 重置按钮样式
    listBtn.classList.add('text-gray-500');
    calendarBtn.classList.add('text-gray-500');
    mapBtn.classList.add('text-gray-500');

    if (view === 'list') {
      listView.classList.remove('hidden');
      listBtn.classList.remove('text-gray-500');
      viewFooter.classList.remove('hidden');
    } else if (view === 'calendar') {
      calendarView.classList.remove('hidden');
      calendarBtn.classList.remove('text-gray-500');
      viewFooter.classList.remove('hidden');
      renderCalendar();
    } else if (view === 'map') {
      mapView.classList.remove('hidden');
      mapBtn.classList.remove('text-gray-500');
      viewFooter.classList.add('hidden');
      renderMap();
    }
    filterEvents();
  }

  // 渲染日历视图
  function renderCalendar() {
    const container = document.getElementById('calendar-container');
    if (!container) return;

    // 使用统一的筛选函数
    const filteredConferences = getFilteredConferences();

    // 按月份分组会议
    const conferencesByMonth = {};
    filteredConferences.forEach(conf => {
      const date = new Date(conf.dateStart);
      const yearMonth = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (!conferencesByMonth[yearMonth]) {
        conferencesByMonth[yearMonth] = [];
      }
      conferencesByMonth[yearMonth].push(conf);
    });

    // 按月份排序
    const sortedMonths = Object.keys(conferencesByMonth).sort();

    container.innerHTML = '';

    sortedMonths.forEach(yearMonth => {
      const [year, month] = yearMonth.split('-');
      const monthName = new Date(year, month - 1).toLocaleString('zh-CN', { month: 'long', year: 'numeric' });
      const conferences = conferencesByMonth[yearMonth];

      const monthSection = document.createElement('div');
      monthSection.className = 'bg-cardbg border border-gray-700 rounded-xl p-6';
      monthSection.innerHTML = `
        <h3 class="text-xl font-bold text-white mb-4">${monthName}</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" data-month="${yearMonth}">
        </div>
      `;

      const grid = monthSection.querySelector(`[data-month="${yearMonth}"]`);
      
      conferences.forEach(conf => {
        const date = new Date(conf.dateStart);
        const day = date.getDate();
        const monthShort = date.toLocaleString('en-US', { month: 'short' }).toUpperCase();
        
        const typeClassMap = {
          'life': 'tag-life',
          'earth': 'tag-earth',
          'it': 'tag-it',
          'physical': 'tag-physical',
          'social': 'tag-social',
          'medicine': 'tag-medicine',
          'other': 'tag-other'
        };
        const typeClass = typeClassMap[conf.type] || 'tag-other';

        const card = document.createElement('div');
        card.className = 'conference-card bg-darkbg border border-gray-700 rounded-lg p-4 hover:border-brand/50 transition cursor-pointer group';
        card.dataset.type = conf.type;
        card.dataset.dateStart = conf.dateStart;
        card.onclick = () => window.location.href = conf.url;
        
        card.innerHTML = `
          <div class="flex items-start gap-3">
            <div class="flex-shrink-0 flex flex-col items-center justify-center bg-cardbg w-12 h-12 rounded-lg border border-gray-600 group-hover:border-brand group-hover:text-brand transition">
              <span class="text-xs font-bold text-gray-500 group-hover:text-brand/70">${monthShort}</span>
              <span class="text-lg font-bold text-white group-hover:text-brand">${day}</span>
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-2 mb-1 flex-wrap">
                ${conf.tags && conf.tags.length > 0 ? 
                  conf.tags.slice(0, 1).map(tag => `<span class="text-xs px-2 py-0.5 rounded ${typeClass}">${tag}</span>`).join('') :
                  `<span class="text-xs px-2 py-0.5 rounded ${typeClass}">${conf.discipline}</span>`
                }
              </div>
              <h4 class="text-sm font-bold text-white group-hover:text-brand transition mb-1 line-clamp-2">${conf.title}</h4>
              <p class="text-xs text-gray-400">📍 ${conf.location}</p>
              ${conf.deadline && conf.deadline !== 'N/A' ? 
                `<p class="text-xs mt-1 ${new Date(conf.deadline) < new Date() ? 'text-gray-600' : 'text-orange-400'}">⚠️ 截稿: ${conf.deadline}</p>` : 
                ''
              }
            </div>
          </div>
        `;
        
        grid.appendChild(card);
      });

      container.appendChild(monthSection);
    });

    if (sortedMonths.length === 0) {
      container.innerHTML = `
        <div class="bg-cardbg border border-gray-700 rounded-xl p-8 text-center">
          <p class="text-gray-400 mb-4">暂无会议信息</p>
          <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission.yml" 
             target="_blank" 
             class="inline-block bg-brand hover:bg-brand-light text-white px-6 py-2 rounded-lg font-medium transition">
            提交第一个会议
          </a>
        </div>
      `;
    }
  }

  // 建立标签到学科领域的映射
  function buildTagDisciplineMap() {
    const tagDisciplineMap = new Map(); // tag -> Set of disciplines
    
    conferencesData.forEach(conf => {
      if (conf.tags && Array.isArray(conf.tags) && conf.type) {
        conf.tags.forEach(tag => {
          const tagKey = tag.trim();
          if (tagKey) {
            if (!tagDisciplineMap.has(tagKey)) {
              tagDisciplineMap.set(tagKey, new Set());
            }
            tagDisciplineMap.get(tagKey).add(conf.type);
          }
        });
      }
    });
    
    return tagDisciplineMap;
  }
  
  // 初始化标签过滤选项
  function initTagsFilter() {
    const tagsContainer = document.getElementById('tags-filter-container');
    if (!tagsContainer) return;
    
    // 建立标签到学科领域的映射
    const tagDisciplineMap = buildTagDisciplineMap();
    
    // 获取选中的学科领域
    const selectedDisciplines = Array.from(document.querySelectorAll('.discipline-filter:checked'))
      .map(cb => cb.value);
    
    // 收集应该显示的标签（属于选中学科领域的标签）
    const visibleTags = new Set();
    tagDisciplineMap.forEach((disciplines, tag) => {
      // 如果标签属于至少一个选中的学科领域，则显示
      if (selectedDisciplines.length === 0 || Array.from(disciplines).some(d => selectedDisciplines.includes(d))) {
        visibleTags.add(tag);
      }
    });
    
    // 按字母顺序排序
    const sortedTags = Array.from(visibleTags).sort();
    
    // 生成标签选项
    tagsContainer.innerHTML = '';
    sortedTags.forEach(tag => {
      const label = document.createElement('label');
      label.className = 'flex items-center gap-2 cursor-pointer';
      label.innerHTML = `
        <input type="checkbox" checked value="${tag.replace(/"/g, '&quot;')}" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand tag-filter" onchange="filterEvents()">
        <span class="text-sm">${tag}</span>
      `;
      tagsContainer.appendChild(label);
    });
    
    if (sortedTags.length === 0) {
      tagsContainer.innerHTML = '<p class="text-xs text-gray-500">请先选择学科领域</p>';
    }
  }
  
  // 处理学科领域变化
  function handleDisciplineChange() {
    // 取消清除框的勾选
    const clearCheckbox = document.getElementById('clear-all-disciplines');
    if (clearCheckbox) {
      clearCheckbox.checked = false;
    }
    
    // 更新全选框状态
    updateSelectAllCheckbox();
    
    // 更新标签显示
    initTagsFilter();
    
    // 触发筛选
    filterEvents();
  }
  
  // 全选所有学科领域
  function handleSelectAllDisciplines() {
    const selectAllCheckbox = document.getElementById('select-all-disciplines');
    const clearCheckbox = document.getElementById('clear-all-disciplines');
    
    if (selectAllCheckbox && selectAllCheckbox.checked) {
      // 全选
      document.querySelectorAll('.discipline-filter').forEach(cb => {
        cb.checked = true;
      });
      if (clearCheckbox) {
        clearCheckbox.checked = false;
      }
      updateSelectAllCheckbox();
      initTagsFilter();
      filterEvents();
    } else if (selectAllCheckbox && !selectAllCheckbox.checked) {
      // 如果取消全选，则清除所有
      document.querySelectorAll('.discipline-filter').forEach(cb => {
        cb.checked = false;
      });
      if (clearCheckbox) {
        clearCheckbox.checked = true;
      }
      updateSelectAllCheckbox();
      initTagsFilter();
      filterEvents();
    }
  }
  
  // 清除所有学科领域
  function handleClearAllDisciplines() {
    const clearCheckbox = document.getElementById('clear-all-disciplines');
    const selectAllCheckbox = document.getElementById('select-all-disciplines');
    
    if (clearCheckbox && clearCheckbox.checked) {
      // 清除所有
      document.querySelectorAll('.discipline-filter').forEach(cb => {
        cb.checked = false;
      });
      if (selectAllCheckbox) {
        selectAllCheckbox.checked = false;
      }
      updateSelectAllCheckbox();
      initTagsFilter();
      filterEvents();
    } else if (clearCheckbox && !clearCheckbox.checked) {
      // 如果取消清除，则全选所有
      document.querySelectorAll('.discipline-filter').forEach(cb => {
        cb.checked = true;
      });
      if (selectAllCheckbox) {
        selectAllCheckbox.checked = true;
      }
      updateSelectAllCheckbox();
      initTagsFilter();
      filterEvents();
    }
  }
  
  // 更新全选框状态
  function updateSelectAllCheckbox() {
    const selectAllCheckbox = document.getElementById('select-all-disciplines');
    const disciplineCheckboxes = document.querySelectorAll('.discipline-filter');
    const checkedCount = document.querySelectorAll('.discipline-filter:checked').length;
    
    if (selectAllCheckbox && disciplineCheckboxes.length > 0) {
      selectAllCheckbox.checked = checkedCount === disciplineCheckboxes.length;
    }
  }
  
  // 重置筛选
  function resetFilters() {
    // 重置学科领域（全选）
    document.querySelectorAll('.discipline-filter').forEach(cb => {
      cb.checked = true;
    });
    // 重置全选和清除框
    const selectAllCheckbox = document.getElementById('select-all-disciplines');
    const clearCheckbox = document.getElementById('clear-all-disciplines');
    if (selectAllCheckbox) selectAllCheckbox.checked = true;
    if (clearCheckbox) clearCheckbox.checked = false;
    
    // 更新标签显示
    initTagsFilter();
    
    // 重置标签（全选）
    setTimeout(() => {
      document.querySelectorAll('.tag-filter').forEach(cb => {
        cb.checked = true;
      });
    }, 0);
    
    // 重置状态
    document.getElementById('only-open').checked = false;
    // 重置时间范围
    document.getElementById('date-start-filter').value = '';
    document.getElementById('date-end-filter').value = '';
    filterEvents();
  }

  // 获取筛选后的会议数据
  function getFilteredConferences() {
    // 获取选中的学科领域
    const selectedDisciplines = Array.from(document.querySelectorAll('.discipline-filter:checked'))
      .map(cb => cb.value);
    
    // 获取选中的标签
    const selectedTags = Array.from(document.querySelectorAll('.tag-filter:checked'))
      .map(cb => cb.value);
    
    const onlyOpen = document.getElementById('only-open')?.checked;
    const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
    const dateStartFilter = document.getElementById('date-start-filter')?.value || '';
    const dateEndFilter = document.getElementById('date-end-filter')?.value || '';

    return conferencesData.filter(conf => {
      // 学科领域筛选
      const matchesDiscipline = selectedDisciplines.length === 0 || selectedDisciplines.includes(conf.type);
      
      // 标签筛选（如果选中了标签，会议必须包含至少一个选中的标签）
      let matchesTags = true;
      if (selectedTags.length > 0 && conf.tags && Array.isArray(conf.tags)) {
        matchesTags = conf.tags.some(tag => selectedTags.includes(tag));
      }
      
      // 搜索筛选
      const matchesSearch = searchTerm === '' || 
        conf.title.toLowerCase().includes(searchTerm) ||
        conf.location.toLowerCase().includes(searchTerm) ||
        (conf.tags && conf.tags.some(tag => tag.toLowerCase().includes(searchTerm)));
      
      // 未开始筛选
      let matchesNotStarted = true;
      if (onlyOpen) {
        matchesNotStarted = new Date(conf.dateStart) > new Date();
      }

      // 时间范围筛选
      let matchesDateRange = true;
      if (dateStartFilter || dateEndFilter) {
        const confStartDate = new Date(conf.dateStart);
        const confEndDate = new Date(conf.dateEnd || conf.dateStart);
        
        if (dateStartFilter) {
          const startFilterDate = new Date(dateStartFilter);
          matchesDateRange = matchesDateRange && confEndDate >= startFilterDate;
        }
        if (dateEndFilter) {
          const endFilterDate = new Date(dateEndFilter);
          matchesDateRange = matchesDateRange && confStartDate <= endFilterDate;
        }
      }
      
      return matchesDiscipline && matchesTags && matchesSearch && matchesNotStarted && matchesDateRange;
    });
  }

  // 增强筛选功能
  const originalFilterEvents = window.filterEvents;
  window.filterEvents = function() {
    const filteredConferences = getFilteredConferences();
    
    // 列表视图筛选
    const cards = document.querySelectorAll('.conference-card');
    cards.forEach(card => {
      const cardType = card.dataset.type || '';
      const cardDateStart = card.dataset.dateStart || '';
      const cardDateEnd = card.dataset.dateEnd || cardDateStart;
      const text = card.textContent.toLowerCase();
      
      // 获取选中的学科领域
      const selectedDisciplines = Array.from(document.querySelectorAll('.discipline-filter:checked'))
        .map(cb => cb.value);
      
      // 获取选中的标签
      const selectedTags = Array.from(document.querySelectorAll('.tag-filter:checked'))
        .map(cb => cb.value);
      
      const onlyOpen = document.getElementById('only-open')?.checked;
      const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
      const dateStartFilter = document.getElementById('date-start-filter')?.value || '';
      const dateEndFilter = document.getElementById('date-end-filter')?.value || '';
      
      // 学科领域匹配
      const matchesDiscipline = selectedDisciplines.length === 0 || selectedDisciplines.includes(cardType);
      
      // 标签匹配（需要从卡片中提取标签）
      let matchesTags = true;
      if (selectedTags.length > 0) {
        // 从卡片中提取所有标签文本（包括学科分类标签和细分标签）
        const cardTags = Array.from(card.querySelectorAll('span[class*="tag-"]'))
          .map(el => el.textContent.trim())
          .filter(tag => tag.length > 0);
        matchesTags = cardTags.some(tag => selectedTags.includes(tag));
      }
      
      const matchesSearch = text.includes(searchTerm);
      
      let matchesNotStarted = true;
      if (onlyOpen && cardDateStart) {
        matchesNotStarted = new Date(cardDateStart) > new Date();
      }

      let matchesDateRange = true;
      if (dateStartFilter || dateEndFilter) {
        if (cardDateStart) {
          const confStartDate = new Date(cardDateStart);
          const confEndDate = new Date(cardDateEnd);
          
          if (dateStartFilter) {
            const startFilterDate = new Date(dateStartFilter);
            // 会议结束日期必须在筛选开始日期之后
            matchesDateRange = matchesDateRange && confEndDate >= startFilterDate;
          }
          if (dateEndFilter) {
            const endFilterDate = new Date(dateEndFilter);
            // 会议开始日期必须在筛选结束日期之前
            matchesDateRange = matchesDateRange && confStartDate <= endFilterDate;
          }
        } else {
          matchesDateRange = false;
        }
      }
      
      if (matchesDiscipline && matchesTags && matchesSearch && matchesNotStarted && matchesDateRange) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });

    // 如果当前是日历视图，重新渲染以应用筛选
    if (currentView === 'calendar') {
      renderCalendar();
    }
    
    // 如果当前是地图视图，重新渲染以应用筛选
    if (currentView === 'map') {
      renderMap();
    }
  };

  // 渲染地图视图
  function renderMap() {
    const container = document.getElementById('map-container');
    if (!container) return;

    // 检查API密钥是否配置
    if (!AMAP_KEY || AMAP_KEY === '') {
      container.innerHTML = `
        <div class="flex items-center justify-center h-full text-gray-400">
          <div class="text-center p-6">
            <div class="mb-2 text-4xl">🗺️</div>
            <div class="mb-2 font-semibold">地图功能需要配置高德地图API密钥</div>
            <div class="text-sm text-gray-500 mb-4">请在 _config.yml 中配置 amap_key</div>
            <a href="https://console.amap.com/" target="_blank" class="text-brand hover:underline text-sm">
              前往高德开放平台申请密钥 →
            </a>
          </div>
        </div>
      `;
      return;
    }

    // 如果地图未初始化，先加载高德地图API
    if (!window.AMap) {
      container.innerHTML = `
        <div class="flex items-center justify-center h-full text-gray-400">
          <div class="text-center">
            <div class="mb-2">🗺️</div>
            <div>正在加载地图...</div>
          </div>
        </div>
      `;
      
      // 动态加载高德地图API
      const script = document.createElement('script');
      script.src = `https://webapi.amap.com/maps?v=2.0&key=${AMAP_KEY}&callback=initAMap`;
      script.async = true;
      script.defer = true;
      script.onerror = function() {
        container.innerHTML = `
          <div class="flex items-center justify-center h-full text-gray-400">
            <div class="text-center p-6">
              <div class="mb-2 text-4xl">⚠️</div>
              <div class="mb-2 font-semibold">地图加载失败</div>
              <div class="text-sm text-gray-500 mb-4">请检查API密钥是否正确配置</div>
            </div>
          </div>
        `;
      };
      document.head.appendChild(script);
      
      // 设置回调函数
      window.initAMap = function() {
        initMap();
      };
      
      return;
    }

    initMap();
  }

  // 初始化地图
  function initMap() {
    const container = document.getElementById('map-container');
    if (!container) return;

    // 如果地图已存在，先销毁
    if (mapInstance) {
      mapInstance.destroy();
      mapMarkers = [];
    }

    // 创建地图实例
    mapInstance = new AMap.Map('map-container', {
      zoom: 5,
      center: [104.0, 35.0], // 中国中心位置
      viewMode: '3D',
      mapStyle: 'amap://styles/darkblue' // 深色主题，适配网站风格
    });

    // 获取筛选后的会议
    const filteredConferences = getFilteredConferences();

    if (filteredConferences.length === 0) {
      container.innerHTML = `
        <div class="flex items-center justify-center h-full text-gray-400">
          <div class="text-center">
            <div class="mb-2">🗺️</div>
            <div>暂无符合条件的会议</div>
          </div>
        </div>
      `;
      return;
    }

    // 地址解析和标记点
    const geocoder = new AMap.Geocoder();
    let geocodeCount = 0;
    const totalCount = filteredConferences.length;

    filteredConferences.forEach((conf, index) => {
      // 解析地址（格式：省份 · 城市）
      const address = conf.location.replace(' · ', '');
      
      geocoder.getLocation(address, (status, result) => {
        geocodeCount++;
        
        if (status === 'complete' && result.geocodes.length > 0) {
          const location = result.geocodes[0].location;
          
          // 创建标记点
          const marker = new AMap.Marker({
            position: [location.lng, location.lat],
            title: conf.title,
            map: mapInstance
          });

          // 创建信息窗口
          const infoWindow = new AMap.InfoWindow({
            content: `
              <div style="color: #333; padding: 10px; min-width: 200px;">
                <h3 style="margin: 0 0 8px 0; font-size: 14px; font-weight: bold;">${conf.title}</h3>
                <p style="margin: 4px 0; font-size: 12px; color: #666;">📍 ${conf.location}</p>
                <p style="margin: 4px 0; font-size: 12px; color: #666;">🕒 ${conf.dateStart}${conf.dateEnd !== conf.dateStart ? ' - ' + conf.dateEnd : ''}</p>
                ${conf.deadline && conf.deadline !== 'N/A' ? `<p style="margin: 4px 0; font-size: 12px; color: #f97316;">⚠️ 截稿: ${conf.deadline}</p>` : ''}
                <a href="${conf.url}" target="_blank" style="display: inline-block; margin-top: 8px; padding: 4px 12px; background: #059669; color: white; text-decoration: none; border-radius: 4px; font-size: 12px;">查看详情</a>
              </div>
            `,
            offset: new AMap.Pixel(0, -30)
          });

          marker.on('click', () => {
            infoWindow.open(mapInstance, marker.getPosition());
          });

          mapMarkers.push(marker);
        }

        // 所有地址解析完成后，调整地图视野
        if (geocodeCount === totalCount && mapMarkers.length > 0) {
          const bounds = new AMap.Bounds();
          mapMarkers.forEach(marker => {
            bounds.extend(marker.getPosition());
          });
          mapInstance.setBounds(bounds, false, [50, 50, 50, 50]);
        }
      });
    });
  }
</script>



