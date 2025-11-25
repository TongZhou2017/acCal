---
layout: default
title: 会议列表
permalink: /conferences/
---

# 📅 会议列表

<div class="conferences-list">
  {% assign conferences = site.conferences | sort: 'date_start' | reverse %}
  
  {% if conferences.size > 0 %}
    <ul class="conference-items">
      {% for conference in conferences %}
        {% unless conference.draft %}
          <li class="conference-item">
            <h3><a href="{{ conference.url | relative_url }}">{{ conference.title }}</a></h3>
            <div class="conference-meta">
              <span class="discipline">{{ conference.discipline }}</span>
              <span class="date">{{ conference.date_start }}{% if conference.date_end != conference.date_start %} - {{ conference.date_end }}{% endif %}</span>
              <span class="location">{{ conference.location }}</span>
              {% if conference.deadline != 'N/A' %}
                <span class="deadline">截止: {{ conference.deadline }}</span>
              {% endif %}
            </div>
            <div class="conference-tags">
              {% for tag in conference.tags %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
            <a href="{{ conference.url }}" target="_blank" rel="noopener" class="external-link">官方链接 →</a>
          </li>
        {% endunless %}
      {% endfor %}
    </ul>
  {% else %}
    <p>暂无会议信息。欢迎 <a href="https://github.com/TongZhou2017/acCal/issues/new?template=conference_submission.yml">提交会议</a>！</p>
  {% endif %}
</div>

