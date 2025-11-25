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
        <button class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700">列表视图</button>
        <button class="bg-cardbg border border-gray-600 px-3 py-1 rounded text-sm hover:bg-gray-700 text-gray-500">日历视图</button>
      </div>
    </div>

    <div id="events-container" class="space-y-4">
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
          <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission.yml" 
             target="_blank" 
             class="inline-block bg-brand hover:bg-brand-light text-white px-6 py-2 rounded-lg font-medium transition">
            提交第一个会议
          </a>
        </div>
      {% endif %}
    </div>
    
    <div class="mt-8 text-center">
      <p class="text-gray-500 text-sm">-- 到底了，去 <a href="https://github.com/{{ site.social.github }}" target="_blank" class="text-brand hover:underline">GitHub</a> 提交更多信息吧 --</p>
    </div>
  </section>
</div>

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
      const isDeadlinePassed = deadlineText.includes('截稿') && deadlineText.match(/截稿: (\d{4}-\d{2}-\d{2})/);
      
      const matchesType = selectedTypes.length === 0 || selectedTypes.includes(cardType);
      const matchesSearch = text.includes(searchTerm);
      const matchesDeadline = !onlyOpen || !isDeadlinePassed || (isDeadlinePassed && new Date(isDeadlinePassed[1]) > new Date());
      
      if (matchesType && matchesSearch && matchesDeadline) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  };
</script>


