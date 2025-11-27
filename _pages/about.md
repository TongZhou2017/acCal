---
layout: default
title: 关于
permalink: /about/
---

<div class="max-w-4xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
  <div class="bg-cardbg border border-gray-700 rounded-2xl p-6 md:p-8">
    <h1 class="text-3xl font-bold text-white mb-6">关于 acCal</h1>

    <section class="mb-8">
      <h2 class="text-2xl font-bold text-white mb-4">项目使命</h2>
      <p class="text-gray-300 leading-relaxed">
        acCal 致力于解决国内学术会议信息分散、鱼龙混杂的痛点。我们提供一个开源、可订阅、且经过人工审核的纯净会议日历，帮助科研人员更高效地规划学术日程。
      </p>
    </section>

    <section class="mb-8">
      <h2 class="text-2xl font-bold text-white mb-4">核心原则</h2>
      <div class="grid md:grid-cols-2 gap-4">
        <div class="bg-darkbg border border-gray-700 rounded-lg p-4">
          <h3 class="text-lg font-bold text-brand mb-2">🔓 开源透明</h3>
          <p class="text-gray-300 text-sm">所有代码和数据公开，社区共同维护</p>
        </div>
        <div class="bg-darkbg border border-gray-700 rounded-lg p-4">
          <h3 class="text-lg font-bold text-brand mb-2">✨ 质量优先</h3>
          <p class="text-gray-300 text-sm">严格审核，拒绝掠夺性会议和商业培训</p>
        </div>
        <div class="bg-darkbg border border-gray-700 rounded-lg p-4">
          <h3 class="text-lg font-bold text-brand mb-2">👥 社区驱动</h3>
          <p class="text-gray-300 text-sm">通过 GitHub Issues 提交，自动化流程处理</p>
        </div>
        <div class="bg-darkbg border border-gray-700 rounded-lg p-4">
          <h3 class="text-lg font-bold text-brand mb-2">🆓 免费使用</h3>
          <p class="text-gray-300 text-sm">永远免费，无广告，无商业推广</p>
        </div>
      </div>
    </section>

    <section class="mb-8">
      <h2 class="text-2xl font-bold text-white mb-4">如何参与</h2>
      <div class="space-y-3">
        <a href="https://github.com/{{ site.social.github }}/issues/new?template=conference_submission.yml" 
           target="_blank" 
           class="flex items-center gap-3 p-4 bg-darkbg border border-gray-700 rounded-lg hover:border-brand transition group">
          <span class="text-2xl">📝</span>
          <div class="flex-1">
            <div class="font-medium text-white group-hover:text-brand transition">提交会议信息</div>
            <div class="text-sm text-gray-400">通过 GitHub Issue 提交新的会议</div>
          </div>
          <svg class="w-5 h-5 text-gray-500 group-hover:text-brand transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
          </svg>
        </a>
        <a href="https://github.com/{{ site.social.github }}/issues" 
           target="_blank" 
           class="flex items-center gap-3 p-4 bg-darkbg border border-gray-700 rounded-lg hover:border-brand transition group">
          <span class="text-2xl">🐛</span>
          <div class="flex-1">
            <div class="font-medium text-white group-hover:text-brand transition">报告问题</div>
            <div class="text-sm text-gray-400">反馈 bug 或提出改进建议</div>
          </div>
          <svg class="w-5 h-5 text-gray-500 group-hover:text-brand transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
          </svg>
        </a>
        <a href="https://github.com/{{ site.social.github }}/pulls" 
           target="_blank" 
           class="flex items-center gap-3 p-4 bg-darkbg border border-gray-700 rounded-lg hover:border-brand transition group">
          <span class="text-2xl">💻</span>
          <div class="flex-1">
            <div class="font-medium text-white group-hover:text-brand transition">贡献代码</div>
            <div class="text-sm text-gray-400">参与项目开发和改进</div>
          </div>
          <svg class="w-5 h-5 text-gray-500 group-hover:text-brand transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
          </svg>
        </a>
      </div>
    </section>

    <section class="mb-8">
      <h2 class="text-2xl font-bold text-white mb-4">技术架构</h2>
      <div class="bg-darkbg border border-gray-700 rounded-lg p-4">
        <ul class="space-y-2 text-gray-300">
          <li class="flex items-center gap-2">
            <span class="text-brand">•</span>
            <strong class="text-white">内容管理：</strong> GitHub Issues
          </li>
          <li class="flex items-center gap-2">
            <span class="text-brand">•</span>
            <strong class="text-white">自动化：</strong> GitHub Actions + Python
          </li>
          <li class="flex items-center gap-2">
            <span class="text-brand">•</span>
            <strong class="text-white">前端：</strong> Jekyll + Tailwind CSS
          </li>
          <li class="flex items-center gap-2">
            <span class="text-brand">•</span>
            <strong class="text-white">托管：</strong> GitHub Pages
          </li>
        </ul>
      </div>
    </section>

    <section class="pt-6 border-t border-gray-700">
      <h2 class="text-2xl font-bold text-white mb-4">许可证</h2>
      <p class="text-gray-300">
        本项目采用 MIT 许可证。详见 
        <a href="https://github.com/{{ site.social.github }}/blob/main/LICENSE" 
           target="_blank" 
           class="text-brand hover:text-brand-light underline">LICENSE</a> 文件。
      </p>
    </section>
  </div>
</div>

