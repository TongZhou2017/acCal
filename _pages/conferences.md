---
layout: default
title: 会议列表
permalink: /conferences/
---

<div class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
  <div class="mb-8">
    <h1 class="text-3xl font-bold text-white mb-2">📅 所有会议</h1>
    <p class="text-gray-400">浏览所有已收录的学术会议</p>
  </div>

  <div class="space-y-4">
    {% assign conferences = site.conferences | sort: 'date_start' %}
    
    {% if conferences.size > 0 %}
      {% for conference in conferences %}
        {% unless conference.draft %}
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
               data-type="{{ type_value }}">
            <div class="flex gap-4">
              <div class="flex-shrink-0 flex flex-col items-center justify-center bg-darkbg w-16 h-16 rounded-lg border border-gray-700 group-hover:border-brand group-hover:text-brand transition">
                <span class="text-xs font-bold uppercase tracking-wider text-gray-500 group-hover:text-brand/70">{{ month }}</span>
                <span class="text-2xl font-bold text-white group-hover:text-brand">{{ day }}</span>
              </div>
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-1 flex-wrap">
                  {% if conference.tags.size > 0 %}
                    {% for tag in conference.tags limit: 3 %}
                      <span class="text-xs px-2 py-0.5 rounded {{ type_class }}">{{ tag }}</span>
                    {% endfor %}
                  {% else %}
                    <span class="text-xs px-2 py-0.5 rounded {{ type_class }}">{{ conference.discipline }}</span>
                  {% endif %}
                </div>
                <h3 class="text-lg font-bold text-white group-hover:text-brand transition mb-1">
                  <a href="{{ conference.url | relative_url }}" class="hover:text-brand">{{ conference.title }}</a>
                </h3>
                <div class="flex items-center gap-4 text-sm text-gray-400 flex-wrap mb-2">
                  <span class="flex items-center gap-1">📍 {{ conference.location }}</span>
                  <span class="flex items-center gap-1">🕒 {{ conference.date_start }}{% if conference.date_end != conference.date_start %} - {{ conference.date_end }}{% endif %}</span>
                  {% if conference.deadline != 'N/A' and conference.deadline != '' %}
                    <span class="flex items-center gap-1 {% if deadline_passed %}text-gray-600{% else %}text-orange-400{% endif %}">
                      ⚠️ 截稿: {{ conference.deadline }}
                    </span>
                  {% endif %}
                </div>
                {% if conference.url %}
                  <a href="{{ conference.url }}" target="_blank" rel="noopener" class="text-sm text-brand hover:text-brand-light inline-flex items-center gap-1">
                    访问官方网站 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                  </a>
                {% endif %}
              </div>
              <div class="hidden sm:flex items-center justify-center">
                <a href="{{ conference.url | relative_url }}" class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center text-gray-300 group-hover:bg-brand group-hover:text-white transition">➝</a>
              </div>
            </div>
          </div>
        {% endunless %}
      {% endfor %}
    {% else %}
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
</div>

