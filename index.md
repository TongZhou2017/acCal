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
          <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">学科领域</p>
          <div class="space-y-2">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="eco" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="filterEvents()">
              <span class="text-sm">生态学 (Ecology)</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="evo" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="filterEvents()">
              <span class="text-sm">进化生物学 (Evolution)</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="env" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="filterEvents()">
              <span class="text-sm">环境科学 (Environment)</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" checked value="bio" class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand" onchange="filterEvents()">
              <span class="text-sm">生物信息学 (Bioinfo)</span>
            </label>
          </div>
        </div>

        <div>
          <p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">状态</p>
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" id="only-open" class="form-checkbox text-brand rounded bg-darkbg border-gray-600" onchange="filterEvents()">
            <span class="text-sm">仅显示未截稿</span>
          </label>
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
        <p class="text-gray-400 text-sm mt-1">让学术回归纯粹，把时间还给科研</p>
      </div>
      <div class="flex gap-2">
        <button id="list-view-btn" onclick="switchView('list')" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 transition">列表视图</button>
        <button id="calendar-view-btn" onclick="switchView('calendar')" class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 text-gray-500 transition">日历视图</button>
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
          
          {% assign type_class = "tag-bio" %}
          {% if conference.discipline contains "生态" or conference.discipline contains "Ecology" %}
            {% assign type_class = "tag-eco" %}
            {% assign type_value = "eco" %}
          {% elsif conference.discipline contains "进化" or conference.discipline contains "Evolution" %}
            {% assign type_class = "tag-evo" %}
            {% assign type_value = "evo" %}
          {% elsif conference.discipline contains "环境" or conference.discipline contains "Environment" %}
            {% assign type_class = "tag-env" %}
            {% assign type_value = "env" %}
          {% else %}
            {% assign type_value = "bio" %}
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
          <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission" 
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
    
    <div class="mt-8 text-center">
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
      {% assign type_value = "bio" %}
      {% if conference.discipline contains "生态" or conference.discipline contains "Ecology" %}
        {% assign type_value = "eco" %}
      {% elsif conference.discipline contains "进化" or conference.discipline contains "Evolution" %}
        {% assign type_value = "evo" %}
      {% elsif conference.discipline contains "环境" or conference.discipline contains "Environment" %}
        {% assign type_value = "env" %}
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

  // 视图切换
  function switchView(view) {
    currentView = view;
    const listView = document.getElementById('list-view');
    const calendarView = document.getElementById('calendar-view');
    const listBtn = document.getElementById('list-view-btn');
    const calendarBtn = document.getElementById('calendar-view-btn');

    if (view === 'list') {
      listView.classList.remove('hidden');
      calendarView.classList.add('hidden');
      listBtn.classList.remove('text-gray-500');
      calendarBtn.classList.add('text-gray-500');
    } else {
      listView.classList.add('hidden');
      calendarView.classList.remove('hidden');
      listBtn.classList.add('text-gray-500');
      calendarBtn.classList.remove('text-gray-500');
      renderCalendar();
    }
    filterEvents();
  }

  // 渲染日历视图
  function renderCalendar() {
    const container = document.getElementById('calendar-container');
    if (!container) return;

    // 获取筛选条件
    const checkedBoxes = document.querySelectorAll('aside input[type="checkbox"]:checked');
    const selectedTypes = Array.from(checkedBoxes)
      .filter(cb => cb.value && cb.id !== 'only-open')
      .map(cb => cb.value);
    const onlyOpen = document.getElementById('only-open')?.checked;
    const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';

    // 筛选会议
    const filteredConferences = conferencesData.filter(conf => {
      const matchesType = selectedTypes.length === 0 || selectedTypes.includes(conf.type);
      const matchesSearch = searchTerm === '' || 
        conf.title.toLowerCase().includes(searchTerm) ||
        conf.location.toLowerCase().includes(searchTerm) ||
        (conf.tags && conf.tags.some(tag => tag.toLowerCase().includes(searchTerm)));
      
      let matchesDeadline = true;
      if (onlyOpen && conf.deadline && conf.deadline !== 'N/A') {
        matchesDeadline = new Date(conf.deadline) > new Date();
      }
      
      return matchesType && matchesSearch && matchesDeadline;
    });

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
        
        const typeClass = conf.type === 'eco' ? 'tag-eco' : 
                          conf.type === 'evo' ? 'tag-evo' :
                          conf.type === 'env' ? 'tag-env' : 'tag-bio';

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
          <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission" 
             target="_blank" 
             class="inline-block bg-brand hover:bg-brand-light text-white px-6 py-2 rounded-lg font-medium transition">
            提交第一个会议
          </a>
        </div>
      `;
    }
  }

  // 重置筛选
  function resetFilters() {
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      if (cb.id !== 'only-open') {
        cb.checked = true;
      } else {
        cb.checked = false;
      }
    });
    filterEvents();
  }

  // 增强筛选功能
  const originalFilterEvents = window.filterEvents;
  window.filterEvents = function() {
    const checkedBoxes = document.querySelectorAll('aside input[type="checkbox"]:checked');
    const selectedTypes = Array.from(checkedBoxes)
      .filter(cb => cb.value && cb.id !== 'only-open')
      .map(cb => cb.value);
    const onlyOpen = document.getElementById('only-open')?.checked;
    const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
    
    const cards = document.querySelectorAll('.conference-card');
    cards.forEach(card => {
      const cardType = card.dataset.type || '';
      const text = card.textContent.toLowerCase();
      const deadlineText = card.textContent;
      const deadlineMatch = deadlineText.match(/截稿: (\d{4}-\d{2}-\d{2})/);
      const isDeadlinePassed = deadlineMatch && new Date(deadlineMatch[1]) < new Date();
      
      const matchesType = selectedTypes.length === 0 || selectedTypes.includes(cardType);
      const matchesSearch = text.includes(searchTerm);
      const matchesDeadline = !onlyOpen || !isDeadlinePassed || (deadlineMatch && new Date(deadlineMatch[1]) > new Date());
      
      if (matchesType && matchesSearch && matchesDeadline) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });

    // 如果当前是日历视图，重新渲染以应用筛选
    if (currentView === 'calendar') {
      renderCalendar();
    }
  };
</script>


