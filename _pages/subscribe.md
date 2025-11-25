---
layout: default
title: 邮件订阅
permalink: /subscribe/
---

<div class="max-w-4xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
  <div class="bg-cardbg border border-gray-700 rounded-2xl p-6 md:p-8">
    <h1 class="text-3xl font-bold text-white mb-2">📧 邮件订阅</h1>
    <p class="text-gray-400 mb-8">订阅学术会议信息，不错过任何重要会议</p>

    <!-- RSS订阅 -->
    <section class="mb-8 pb-8 border-b border-gray-700">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg class="w-6 h-6 text-brand" fill="currentColor" viewBox="0 0 24 24">
          <path d="M6.503 20.752c0 1.794-1.456 3.248-3.251 3.248-1.796 0-3.252-1.454-3.252-3.248 0-1.794 1.456-3.248 3.252-3.248 1.795.001 3.251 1.454 3.251 3.248zm-6.503-12.572v4.811c6.05.062 10.96 4.966 11.022 11.009h4.817c-.062-8.71-7.118-15.758-15.839-15.82zm0-3.368c10.58.046 19.152 8.594 19.183 19.188h4.817c-.03-13.231-10.755-23.954-24-24v4.812z"/>
        </svg>
        RSS订阅
      </h2>
      <p class="text-gray-300 mb-4">使用RSS阅读器订阅所有会议更新</p>
      <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center">
        <a href="{{ '/feed.xml' | relative_url }}" 
           target="_blank"
           class="inline-flex items-center gap-2 bg-brand hover:bg-brand-light text-white px-6 py-3 rounded-lg font-medium transition">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M6.503 20.752c0 1.794-1.456 3.248-3.251 3.248-1.796 0-3.252-1.454-3.252-3.248 0-1.794 1.456-3.248 3.252-3.248 1.795.001 3.251 1.454 3.251 3.248zm-6.503-12.572v4.811c6.05.062 10.96 4.966 11.022 11.009h4.817c-.062-8.71-7.118-15.758-15.839-15.82zm0-3.368c10.58.046 19.152 8.594 19.183 19.188h4.817c-.03-13.231-10.755-23.954-24-24v4.812z"/>
          </svg>
          订阅RSS Feed
        </a>
        <span class="text-sm text-gray-400">RSS地址: <code class="bg-darkbg px-2 py-1 rounded text-brand">{{ site.url }}{{ site.baseurl }}/feed.xml</code></span>
      </div>
    </section>

    <!-- 邮件订阅表单 -->
    <section>
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg class="w-6 h-6 text-brand" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
        </svg>
        邮件订阅
      </h2>
      <p class="text-gray-300 mb-6">通过邮件接收会议信息，可自定义订阅的学科领域和提醒设置</p>

      <form id="subscribe-form" class="space-y-6">
        <!-- 邮箱输入 -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-300 mb-2">
            邮箱地址 <span class="text-red-400">*</span>
          </label>
          <input type="email" 
                 id="email" 
                 name="email" 
                 required
                 placeholder="your.email@example.com"
                 class="w-full bg-darkbg border border-gray-600 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-brand focus:ring-2 focus:ring-brand/20">
          <p class="text-xs text-gray-500 mt-1">我们将通过此邮箱发送会议信息和提醒</p>
        </div>

        <!-- 学科领域选择 -->
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-3">
            订阅的学科领域 <span class="text-red-400">*</span>
          </label>
          <p class="text-xs text-gray-500 mb-3">选择您感兴趣的学科领域，我们将只发送相关会议信息</p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <label class="flex items-center gap-3 p-3 bg-darkbg border border-gray-600 rounded-lg cursor-pointer hover:border-brand transition">
              <input type="checkbox" 
                     name="disciplines" 
                     value="eco" 
                     class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand"
                     checked>
              <div>
                <div class="text-white font-medium">生态学</div>
                <div class="text-xs text-gray-400">Ecology</div>
              </div>
            </label>
            <label class="flex items-center gap-3 p-3 bg-darkbg border border-gray-600 rounded-lg cursor-pointer hover:border-brand transition">
              <input type="checkbox" 
                     name="disciplines" 
                     value="evo" 
                     class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand"
                     checked>
              <div>
                <div class="text-white font-medium">进化生物学</div>
                <div class="text-xs text-gray-400">Evolution</div>
              </div>
            </label>
            <label class="flex items-center gap-3 p-3 bg-darkbg border border-gray-600 rounded-lg cursor-pointer hover:border-brand transition">
              <input type="checkbox" 
                     name="disciplines" 
                     value="env" 
                     class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand"
                     checked>
              <div>
                <div class="text-white font-medium">环境科学</div>
                <div class="text-xs text-gray-400">Environment</div>
              </div>
            </label>
            <label class="flex items-center gap-3 p-3 bg-darkbg border border-gray-600 rounded-lg cursor-pointer hover:border-brand transition">
              <input type="checkbox" 
                     name="disciplines" 
                     value="bio" 
                     class="form-checkbox text-brand rounded bg-darkbg border-gray-600 focus:ring-brand"
                     checked>
              <div>
                <div class="text-white font-medium">生物信息学</div>
                <div class="text-xs text-gray-400">Bioinformatics</div>
              </div>
            </label>
          </div>
        </div>

        <!-- 默认提醒设置 -->
        <div>
          <label for="default-reminder-days" class="block text-sm font-medium text-gray-300 mb-2">
            默认提前提醒天数
          </label>
          <div class="flex items-center gap-4">
            <input type="number" 
                   id="default-reminder-days" 
                   name="default_reminder_days" 
                   value="30" 
                   min="1" 
                   max="365"
                   class="w-24 bg-darkbg border border-gray-600 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-brand focus:ring-2 focus:ring-brand/20">
            <span class="text-gray-400">天</span>
          </div>
          <p class="text-xs text-gray-500 mt-1">在会议开始前多少天发送提醒邮件（默认30天）</p>
        </div>

        <!-- 单个会议提醒设置 -->
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-3">
            为特定会议设置提醒
          </label>
          <p class="text-xs text-gray-500 mb-3">为感兴趣的会议设置个性化的提醒时间</p>
          <div id="conference-reminders" class="space-y-3">
            <!-- 动态添加的会议提醒项 -->
          </div>
          <button type="button" 
                  onclick="addConferenceReminder()"
                  class="mt-3 text-sm text-brand hover:text-brand-light flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
            </svg>
            添加会议提醒
          </button>
        </div>

        <!-- 提交按钮 -->
        <div class="pt-4 border-t border-gray-700">
          <button type="submit" 
                  class="w-full bg-brand hover:bg-brand-light text-white px-6 py-3 rounded-lg font-medium transition shadow-lg shadow-brand/20">
            提交订阅
          </button>
          <p class="text-xs text-gray-500 mt-3 text-center">
            提交后，我们将通过GitHub Issue处理您的订阅请求，并在24小时内发送确认邮件
          </p>
        </div>
      </form>
    </section>

    <!-- 说明信息 -->
    <section class="mt-8 pt-8 border-t border-gray-700">
      <h3 class="text-lg font-bold text-white mb-4">📋 订阅说明</h3>
      <div class="bg-darkbg border border-gray-700 rounded-lg p-4 space-y-2 text-sm text-gray-300">
        <p><strong class="text-white">邮件类型：</strong></p>
        <ul class="list-disc list-inside ml-4 space-y-1">
          <li>新会议通知：当有新的会议被添加到日历中时</li>
          <li>会议提醒：在会议开始前按您设置的天数发送提醒</li>
          <li>截稿提醒：在摘要截稿日期前7天发送提醒</li>
        </ul>
        <p class="pt-2"><strong class="text-white">取消订阅：</strong>回复邮件中的取消链接即可</p>
        <p><strong class="text-white">隐私保护：</strong>我们不会分享您的邮箱地址给第三方</p>
      </div>
    </section>
  </div>
</div>

<!-- 会议选择模态框 -->
<div id="conference-select-modal" class="fixed inset-0 bg-black/80 hidden items-center justify-center z-[100] backdrop-blur-sm" onclick="closeConferenceModal()">
  <div class="bg-cardbg w-full max-w-2xl rounded-2xl border border-gray-700 shadow-2xl overflow-hidden transform transition-all scale-95" onclick="event.stopPropagation()">
    <div class="p-6">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-xl font-bold text-white">选择会议</h3>
        <button onclick="closeConferenceModal()" class="text-gray-400 hover:text-white">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <div class="max-h-96 overflow-y-auto space-y-2">
        {% assign conferences = site.conferences | sort: 'date_start' %}
        {% for conference in conferences %}
          {% unless conference.draft %}
            <button type="button"
                    onclick="selectConference('{{ conference.name }}', '{{ conference.title }}', '{{ conference.date_start }}')"
                    class="w-full text-left p-3 bg-darkbg border border-gray-600 rounded-lg hover:border-brand transition">
              <div class="font-medium text-white">{{ conference.title }}</div>
              <div class="text-sm text-gray-400">{{ conference.date_start }} · {{ conference.location }}</div>
            </button>
          {% endunless %}
        {% endfor %}
      </div>
    </div>
  </div>
</div>

<script>
  let reminderCounter = 0;
  let selectedConferenceId = null;

  function addConferenceReminder() {
    document.getElementById('conference-select-modal').classList.remove('hidden');
    document.getElementById('conference-select-modal').classList.add('flex');
  }

  function closeConferenceModal() {
    document.getElementById('conference-select-modal').classList.add('hidden');
    document.getElementById('conference-select-modal').classList.remove('flex');
  }

  function selectConference(id, title, dateStart) {
    selectedConferenceId = id;
    const container = document.getElementById('conference-reminders');
    const reminderId = 'reminder-' + reminderCounter++;
    
    const reminderDiv = document.createElement('div');
    reminderDiv.id = reminderId;
    reminderDiv.className = 'flex items-start gap-3 p-3 bg-darkbg border border-gray-600 rounded-lg';
    reminderDiv.innerHTML = `
      <div class="flex-1">
        <div class="text-white font-medium text-sm">${title}</div>
        <div class="text-xs text-gray-400 mt-1">会议日期: ${dateStart}</div>
        <div class="mt-2 flex items-center gap-2">
          <label class="text-xs text-gray-400">提前</label>
          <input type="number" 
                 name="conference_reminder_days[${id}]" 
                 value="30" 
                 min="1" 
                 max="365"
                 class="w-20 bg-cardbg border border-gray-600 rounded px-2 py-1 text-white text-sm focus:outline-none focus:border-brand">
          <label class="text-xs text-gray-400">天提醒</label>
        </div>
      </div>
      <button type="button" 
              onclick="removeReminder('${reminderId}')"
              class="text-gray-400 hover:text-red-400">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    `;
    
    container.appendChild(reminderDiv);
    closeConferenceModal();
  }

  function removeReminder(id) {
    document.getElementById(id).remove();
  }

  // 表单提交处理
  document.getElementById('subscribe-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const disciplines = Array.from(document.querySelectorAll('input[name="disciplines"]:checked')).map(cb => cb.value);
    const defaultReminderDays = document.getElementById('default-reminder-days').value;
    
    // 收集会议提醒设置
    const conferenceReminders = {};
    document.querySelectorAll('[name^="conference_reminder_days"]').forEach(input => {
      const match = input.name.match(/\[(.+)\]/);
      if (match) {
        conferenceReminders[match[1]] = input.value;
      }
    });

    if (disciplines.length === 0) {
      alert('请至少选择一个学科领域');
      return;
    }

    // 生成GitHub Issue内容
    const issueTitle = `[订阅请求] ${email}`;
    const issueBody = `## 邮件订阅请求

**邮箱地址：** ${email}

**订阅的学科领域：**
${disciplines.map(d => {
  const names = {
    'eco': '生态学 (Ecology)',
    'evo': '进化生物学 (Evolution)',
    'env': '环境科学 (Environment)',
    'bio': '生物信息学 (Bioinformatics)'
  };
  return `- ${names[d]}`;
}).join('\n')}

**默认提前提醒天数：** ${defaultReminderDays} 天

${Object.keys(conferenceReminders).length > 0 ? `**特定会议提醒设置：**
${Object.entries(conferenceReminders).map(([id, days]) => {
  // 这里需要从会议数据中获取标题
  return `- 会议ID: ${id}, 提前 ${days} 天提醒`;
}).join('\n')}` : ''}

---

*此订阅请求由网站表单自动生成*`;

    // 创建GitHub Issue链接
    const githubUrl = `https://github.com/{{ site.social.github }}/issues/new?title=${encodeURIComponent(issueTitle)}&body=${encodeURIComponent(issueBody)}&labels=subscription`;
    
    // 打开新窗口
    window.open(githubUrl, '_blank');
    
    // 显示成功消息
    alert('订阅请求已提交！我们将在24小时内处理您的订阅并发送确认邮件。');
    
    // 重置表单
    this.reset();
    document.getElementById('conference-reminders').innerHTML = '';
    reminderCounter = 0;
  });
</script>

