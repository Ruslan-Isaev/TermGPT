<p>TermGPT - Инструмент для работы с ChatGPT в Терминале Windows или Linux</p>
<h2 id="-">Возможности</h2>
<ul>
<li><p><strong>Поиск текста в ChatGPT:</strong>
Для простого запроса используйте команду:</p>
<pre><code><span class="hljs-attribute">gpt YOURTEXT</span>
</code></pre><p>Замените <code>YOURTEXT</code> на строку, которую вы хотите отправить.</p>
</li>
<li><p><strong>Поиск текста с переносом строк:</strong>
Чтобы отправить несколько строк текста, используйте следующий формат:</p>
<pre><code>gpt <span class="hljs-string">"</span>
&gt;YOURTEXT
&gt;YOURTEXT
&gt;YOURTEXT<span class="hljs-string">"</span>
</code></pre><p>Вместо <code>YOURTEXT</code> вы можете указать как одиночные фразы, так и более длинные запросы.</p>
</li>
<li><p><strong>Просмотр доступных команд:</strong>
Чтобы увидеть список всех доступных команд, просто введите:</p>
<pre><code><span class="hljs-attribute">gpt</span>
</code></pre></li>
<li><p><strong>Запуск промта из файла:</strong>
Вы можете загружать текстовые запросы из файла с помощью команды:</p>
<pre><code>gpt <span class="hljs-comment">--file YOURPATH</span>
</code></pre><p>Замените <code>YOURPATH</code> на путь к файлу, содержащему ваш запрос.</p>
</li>
</ul>
<h2 id="-">Установка</h2>
<pre><code>pip install git+https:<span class="hljs-regexp">//gi</span>thub.com<span class="hljs-regexp">/Ruslan-Isaev/</span>TermGPT
</code></pre><p><strong>Приятного пользования!</strong></p>
