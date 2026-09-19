/* =============================================
   SUBHRAJEET SWAIN — CINEMATIC PORTFOLIO JS
   GSAP · Lenis · Typewriter · Boot Intro
   ============================================= */

(function () {
  'use strict';

  // ─────────────────────────────────────────
  // 1. BOOT / INTRO SCREEN
  // ─────────────────────────────────────────
  const introScreen = document.getElementById('intro-screen');
  const mainSite = document.getElementById('main-site');

  const bootLines = [
    { text: '> Initializing portfolio system...', cls: 'boot-accent' },
    { text: '> Loading modules: QA · Python · SQL · Testing', cls: '' },
    { text: '> Connecting to subhrajeet@portfolio...', cls: '' },
    { text: '> Verifying credentials... <span class="boot-success">authenticated</span>', cls: '' },
    { text: '> Fetching experience data... <span class="boot-success">1 year @ Team Pumpkin</span>', cls: '' },
    { text: '> Loading skills matrix... <span class="boot-success">done</span>', cls: '' },
    { text: '> Compiling education records... <span class="boot-success">MCA · BCA</span>', cls: '' },
    { text: '> Running test suite... <span class="boot-success">7/7 PASS</span>', cls: '' },
    { text: '> <span class="boot-warn">Build complete.</span> Launching portfolio ▶', cls: '' },
  ];

  function runBootSequence() {
    // Skip if already seen
    if (sessionStorage.getItem('intro_seen')) {
      if (introScreen) introScreen.style.display = 'none';
      if (mainSite) { mainSite.style.opacity = '1'; mainSite.style.visibility = 'visible'; }
      initMainSite();
      return;
    }

    const bootContent = document.getElementById('boot-content');
    if (!bootContent) return;

    let i = 0;
    function showNextLine() {
      if (i >= bootLines.length) {
        // Boot done — transition to main
        sessionStorage.setItem('intro_seen', 'true');
        setTimeout(() => {
          document.documentElement.classList.add('intro-done');
          setTimeout(initMainSite, 800);
        }, 600);
        return;
      }

      const line = document.createElement('div');
      line.className = 'boot-line';
      if (bootLines[i].cls) line.classList.add(bootLines[i].cls);
      line.innerHTML = bootLines[i].text;
      bootContent.appendChild(line);

      // Slight delay then reveal
      requestAnimationFrame(() => {
        setTimeout(() => line.classList.add('visible'), 50);
      });

      i++;
      const delay = 250 + Math.random() * 200;
      setTimeout(showNextLine, delay);
    }

    showNextLine();
  }

  // ─────────────────────────────────────────
  // 2. LENIS SMOOTH SCROLL
  // ─────────────────────────────────────────
  let lenis;

  function initLenis() {
    if (typeof Lenis === 'undefined') return;
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smooth: true,
    });
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Sync with GSAP ScrollTrigger
    if (typeof ScrollTrigger !== 'undefined') {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }

  // ─────────────────────────────────────────
  // 3. NAVBAR
  // ─────────────────────────────────────────
  function initNavbar() {
    const burger = document.getElementById('nav-burger');
    const navLinks = document.getElementById('nav-links');
    if (burger && navLinks) {
      burger.addEventListener('click', () => {
        navLinks.classList.toggle('open');
      });
      // Close on link click
      navLinks.querySelectorAll('.nav-link').forEach((link) => {
        link.addEventListener('click', () => navLinks.classList.remove('open'));
      });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener('click', (e) => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
          e.preventDefault();
          if (lenis) {
            lenis.scrollTo(target, { offset: -70 });
          } else {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
      });
    });
  }

  // ─────────────────────────────────────────
  // 4. HERO GREETING ANIMATION
  // ─────────────────────────────────────────
  function initGreeting() {
    const greetings = ['Namaste', 'Hello', 'नमस्ते', 'ନମସ୍କାର', 'Bonjour', 'Hola', 'こんにちは'];
    const wordEl = document.getElementById('greeting-word');
    const greetingEl = document.getElementById('hero-greeting');
    if (!wordEl || !greetingEl) return;

    let idx = 0;

    function showGreeting() {
      if (idx >= greetings.length) {
        // Fade out greeting, reveal hero content
        gsap.to(greetingEl, { opacity: 0, duration: 0.6, onComplete: () => {
          greetingEl.style.display = 'none';
          revealHeroContent();
        }});
        return;
      }

      wordEl.textContent = greetings[idx];
      gsap.fromTo(wordEl,
        { opacity: 0, scale: 0.8 },
        { opacity: 1, scale: 1, duration: 0.35, ease: 'back.out(1.5)',
          onComplete: () => {
            gsap.to(wordEl, { opacity: 0, scale: 1.1, duration: 0.25, delay: 0.3,
              onComplete: () => { idx++; showGreeting(); }
            });
          }
        }
      );
    }

    showGreeting();
  }

  function revealHeroContent() {
    const heroContent = document.getElementById('hero-content');
    const heroCard = document.getElementById('hero-card');

    if (heroContent) {
      gsap.to(heroContent, { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out' });
    }
    if (heroCard) {
      gsap.to(heroCard, { opacity: 1, y: 0, duration: 0.8, delay: 0.3, ease: 'power3.out' });
    }

    // Start typewriter after hero reveals
    setTimeout(initTypewriter, 800);
  }

  // ─────────────────────────────────────────
  // 5. TYPEWRITER
  // ─────────────────────────────────────────
  function initTypewriter() {
    const el = document.getElementById('hero-typewriter');
    if (!el) return;

    const phrases = [
      'I write test cases. Systems deliver quality.',
      'Manual Testing · Test Case Design · Bug Tracking',
      'Python · C · C++ · SQL · MySQL',
      '1 Year QA Intern @ Team Pumpkin (Tech.)',
      'Building the E-Hospital Management System',
      'Power BI · Tableau · MS Excel Analytics',
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;

    function type() {
      const current = phrases[phraseIdx];

      if (isDeleting) {
        el.textContent = current.substring(0, charIdx - 1);
        charIdx--;
      } else {
        el.textContent = current.substring(0, charIdx + 1);
        charIdx++;
      }

      let delay = isDeleting ? 30 : 55;

      if (!isDeleting && charIdx === current.length) {
        delay = 2200;
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        delay = 400;
      }

      setTimeout(type, delay);
    }

    type();
  }

  // ─────────────────────────────────────────
  // 6. TERMINAL ABOUT ANIMATION
  // ─────────────────────────────────────────
  function initTerminal() {
    const lines = document.querySelectorAll('#terminal-body .tline');
    if (!lines.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const body = entry.target;
          const tlines = body.querySelectorAll('.tline');
          tlines.forEach((line) => {
            const delay = parseInt(line.getAttribute('data-delay') || '0', 10);
            setTimeout(() => line.classList.add('visible'), delay);
          });
          observer.unobserve(body);
        }
      });
    }, { threshold: 0.3 });

    const termBody = document.getElementById('terminal-body');
    if (termBody) observer.observe(termBody);
  }

  // ─────────────────────────────────────────
  // 7. ROTATING HEADLINE
  // ─────────────────────────────────────────
  function initHeadline() {
    const wordEl = document.getElementById('headline-word');
    if (!wordEl) return;

    const words = [
      'Zero Defects',
      'Quality First',
      'Tested & Verified',
      'Bug-Free Code',
      'Data-Driven',
      'Pixel Perfect',
      'Production Ready',
    ];

    let idx = 0;

    setInterval(() => {
      gsap.to(wordEl, {
        opacity: 0, y: -20, duration: 0.35,
        onComplete: () => {
          idx = (idx + 1) % words.length;
          wordEl.textContent = words[idx];
          gsap.fromTo(wordEl,
            { opacity: 0, y: 20 },
            { opacity: 1, y: 0, duration: 0.35 }
          );
        }
      });
    }, 2500);
  }

  // ─────────────────────────────────────────
  // 8. GSAP SCROLL REVEALS
  // ─────────────────────────────────────────
  function initScrollReveals() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // General reveal
    gsap.utils.toArray('.reveal').forEach((el) => {
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          once: true,
        },
      });
    });

    // Skill bars
    document.querySelectorAll('.skill-fill').forEach((bar) => {
      ScrollTrigger.create({
        trigger: bar,
        start: 'top 90%',
        once: true,
        onEnter: () => bar.classList.add('animated'),
      });
    });
  }

  // ─────────────────────────────────────────
  // 9. MAIN INIT
  // ─────────────────────────────────────────
  function initMainSite() {
    initLenis();
    initNavbar();
    initGreeting();
    initTerminal();
    initHeadline();

    // Small delay to let DOM settle
    setTimeout(initScrollReveals, 200);
  }

  // ─────────────────────────────────────────
  // START
  // ─────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runBootSequence);
  } else {
    runBootSequence();
  }
})();
