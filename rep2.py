{
  "name": "femai-advisor",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.2.5",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "autoprefixer": "^10.4.0",
    "eslint": "^8.0.0",
    "eslint-config-next": "14.2.5",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.0.0"
  }
}
```

---

## FILE: tsconfig.json

```json
{
  "compilerOptions": {
    "target": "es2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": false,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "types": ["next", "next/types/global", "next/image-types/global"],
    "paths": { "@/*": ["./*"] },
    "plugins": [{ "name": "next" }]
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

---

## FILE: next-env.d.ts

```ts
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
```

---

## FILE: next.config.mjs

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true
  }
};

export default nextConfig;
```

---

## FILE: postcss.config.mjs

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
};
```

---

## FILE: tailwind.config.ts

```ts
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        lavender: {
          50: "#f7f4ff",
          100: "#efe6ff",
          200: "#ddc8ff",
          300: "#c5a0ff",
          400: "#a470f7",
          500: "#7f4fd4",
          600: "#633bb0",
          700: "#4f318d",
          800: "#3f296f",
          900: "#332359"
        },
        blush: {
          50: "#fff5f7",
          100: "#ffe4ec",
          200: "#ffc7d9",
          300: "#ffa0c0",
          400: "#ff6f9c",
          500: "#f43f75"
        }
      },
      boxShadow: {
        soft: "0 18px 45px rgba(31, 41, 55, 0.08)"
      }
    }
  },
  plugins: []
};

export default config;
```

---

## FILE: .gitignore

```
# Dependencies
node_modules
.pnp
.pnp.js

# Build
.next
out
build
dist

# Env and secrets
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
*.pem

# Debug and logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# IDE and OS
.idea
.vscode
.DS_Store
*.swp
*.swo
Thumbs.db

# Vercel
.vercel

# TypeScript
next-env.d.ts
```

---

## FILE: app/globals.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #f9f5ff;
  --foreground: #111827;
}

body {
  @apply bg-gradient-to-br from-lavender-50 via-white to-blush-50 text-slate-900 antialiased;
}

.glass-card {
  @apply rounded-3xl bg-white/80 shadow-soft backdrop-blur border border-white/60;
}

.pill {
  @apply inline-flex items-center gap-2 rounded-full bg-lavender-50 px-3 py-1 text-xs font-medium text-lavender-700;
}

.primary-btn {
  @apply inline-flex items-center justify-center rounded-full bg-lavender-600 px-5 py-2.5 text-sm font-semibold text-white shadow-md shadow-lavender-400/40 transition hover:bg-lavender-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-lavender-400 focus-visible:ring-offset-2;
}

.secondary-btn {
  @apply inline-flex items-center justify-center rounded-full border border-lavender-200 bg-white/70 px-4 py-2 text-sm font-medium text-lavender-700 shadow-sm transition hover:bg-lavender-50;
}
```

---

## FILE: app/layout.tsx

```tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "FemAI Advisor",
  description:
    "Personalized health, hormone, and financial guidance for women, powered by AI."
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={`${inter.className} min-h-screen bg-gradient-to-br from-lavender-50 via-white to-blush-50 text-slate-900`}
      >
        <div className="flex min-h-screen flex-col">
          <header className="sticky top-0 z-30 border-b border-white/60 bg-white/70 backdrop-blur">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
              <Link href="/" className="flex items-center gap-2">
                <div className="flex h-9 w-9 items-center justify-center rounded-2xl bg-gradient-to-br from-lavender-500 to-blush-400 text-white shadow-soft">
                  <span className="text-lg font-semibold">F</span>
                </div>
                <div className="flex flex-col">
                  <span className="text-sm font-semibold tracking-tight">
                    FemAI Advisor
                  </span>
                  <span className="text-xs text-slate-500">
                    Wellness · Hormones · Money
                  </span>
                </div>
              </Link>
              <nav className="flex items-center gap-1 text-xs sm:text-sm">
                <Link
                  href="/"
                  className="secondary-btn px-3 py-1.5 sm:px-4 sm:py-2"
                >
                  Home
                </Link>
                <Link
                  href="/dashboard"
                  className="secondary-btn px-3 py-1.5 sm:px-4 sm:py-2"
                >
                  Dashboard
                </Link>
                <Link
                  href="/advisor"
                  className="primary-btn px-3 py-1.5 sm:px-4 sm:py-2"
                >
                  AI Advisor
                </Link>
              </nav>
            </div>
          </header>

          <main className="flex-1">
            <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8">
              {children}
            </div>
          </main>

          <footer className="border-t border-white/60 bg-white/60 py-4 text-center text-xs text-slate-500 backdrop-blur">
            FemAI Advisor · Designed for modern femtech wellness
          </footer>
        </div>
      </body>
    </html>
  );
}
```

---

## FILE: app/page.tsx

```tsx
import Link from "next/link";

export default function HomePage() {
  return (
    <div className="grid gap-8 lg:grid-cols-[3fr,2fr] lg:items-center">
      <section className="space-y-8">
        <div className="pill w-fit">
          <span className="h-1.5 w-1.5 rounded-full bg-blush-400" />
          Your AI guide for hormone-aware wellness and smarter spending
        </div>

        <div className="space-y-5">
          <h1 className="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl lg:text-5xl">
            FemAI Advisor
          </h1>
          <p className="text-lg font-medium text-lavender-700 sm:text-xl">
            Your AI guide for hormone-aware wellness and smarter spending.
          </p>
          <p className="max-w-xl text-sm text-slate-600 sm:text-base">
            FemAI helps you understand your energy, hormones, habits, and
            wellness spending through gentle AI insights—so your cycle, daily
            routines, and money all work together instead of against you.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <Link href="/onboarding" className="primary-btn text-sm sm:text-base">
            Enter · Start onboarding
          </Link>
          <Link
            href="/advisor"
            className="secondary-btn text-sm sm:text-base"
          >
            Jump into AI chat
          </Link>
        </div>

        <dl className="grid max-w-xl gap-4 text-xs text-slate-600 sm:grid-cols-3 sm:text-sm">
          <div className="glass-card p-4">
            <dt className="font-medium text-slate-900">Cycle-aware insights</dt>
            <dd className="mt-1 text-slate-600">
              Align sleep, movement, and work with your current phase.
            </dd>
          </div>
          <div className="glass-card p-4">
            <dt className="font-medium text-slate-900">Gentle habit nudges</dt>
            <dd className="mt-1 text-slate-600">
              Small, sustainable changes for energy, mood, and stress.
            </dd>
          </div>
          <div className="glass-card p-4">
            <dt className="font-medium text-slate-900">
              Wellness + money clarity
            </dt>
            <dd className="mt-1 text-slate-600">
              See how your wellness choices and spending patterns connect.
            </dd>
          </div>
        </dl>
      </section>

      <section className="glass-card hidden h-full flex-col justify-between gap-6 p-6 sm:flex">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-lavender-600">
              How it works
            </p>
            <p className="mt-1 text-sm font-semibold text-slate-900">
              Onboarding · Profile · Dashboard · Chat
            </p>
          </div>
          <span className="rounded-full bg-lavender-100 px-3 py-1 text-xs font-medium text-lavender-700">
            Personalized by your inputs
          </span>
        </div>

        <div className="space-y-4 text-xs">
          <div className="rounded-2xl bg-gradient-to-br from-lavender-500 to-blush-400 p-4 text-white shadow-soft">
            <p className="text-[11px] uppercase tracking-wide opacity-80">
              Daily AI tip
            </p>
            <p className="mt-1 text-sm font-semibold">
              &ldquo;Your luteal phase may soften your energy—today is a great
              day for slower tasks, warm meals, and earlier sleep.&rdquo;
            </p>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div className="rounded-2xl bg-white/80 p-3 shadow-sm">
              <p className="text-[11px] font-medium text-slate-500">
                Cycle-aware focus
              </p>
              <p className="mt-2 text-sm font-semibold text-slate-900">
                Follicular · Learn &amp; plan
              </p>
              <p className="mt-1 text-[11px] text-slate-500">
                Use rising energy for deep work, planning, and new habits.
              </p>
            </div>
            <div className="rounded-2xl bg-white/80 p-3 shadow-sm">
              <p className="text-[11px] font-medium text-slate-500">
                Wellness budget preview
              </p>
              <p className="mt-2 text-2xl font-semibold text-slate-900">
                $220
              </p>
              <p className="mt-1 text-[11px] text-slate-500">
                AI helps you split this across therapy, movement, and rest.
              </p>
            </div>
          </div>

        <p className="mt-1 text-[11px] text-slate-500">
          FemAI Advisor is not a medical or financial provider. It&apos;s a
          supportive guide for everyday decisions—always pair with professional
          care.
        </p>
        </div>
      </section>
    </div>
  );
}
```

---

## FILE: app/lib/onboarding.ts

```ts
export type PrimaryGoal =
  | "Energy"
  | "Hormone Balance"
  | "Fitness Consistency"
  | "Stress Management"
  | "Saving Money"
  | "Wellness Budgeting";

export type CyclePhaseOption =
  | "Follicular"
  | "Ovulatory"
  | "Luteal"
  | "Menstrual"
  | "Not sure";

export type TracksCycleOption = "Yes" | "Sometimes" | "No";

export type WellnessSpendCategory =
  | "Gym/Fitness"
  | "Supplements"
  | "Skincare"
  | "Therapy/Mental Health"
  | "Healthy Food"
  | "Wellness Apps"
  | "None yet";

export type EnergyDrainOption =
  | "Work/School"
  | "Hormones"
  | "Poor Sleep"
  | "Stress"
  | "Overthinking"
  | "Busy Schedule";

export type AiPersonaOption =
  | "Supportive Coach"
  | "Scientific Explainer"
  | "Motivational Trainer"
  | "Calm Wellness Guide";

export interface OnboardingProfile {
  name: string;
  ageRange: string;
  primaryGoal: PrimaryGoal;
  tracksCycle: TracksCycleOption;
  currentPhase: CyclePhaseOption;
  wellnessSpending: WellnessSpendCategory[];
  monthlyBudget: number;
  sleepHours: number;
  exerciseDays: number;
  stressLevel: number;
  energyDrain: EnergyDrainOption;
  aiPersona: AiPersonaOption;
}

export const ONBOARDING_STORAGE_KEY = "femai_onboarding_profile";

export function loadOnboardingProfile(): OnboardingProfile | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = window.localStorage.getItem(ONBOARDING_STORAGE_KEY);
    if (!raw) return null;
    return JSON.parse(raw) as OnboardingProfile;
  } catch {
    return null;
  }
}

export function saveOnboardingProfile(profile: OnboardingProfile) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(
      ONBOARDING_STORAGE_KEY,
      JSON.stringify(profile)
    );
  } catch {
    // ignore write errors
  }
}
```

---

## FILE: app/onboarding/page.tsx

```tsx
"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";
import {
  AiPersonaOption,
  EnergyDrainOption,
  PrimaryGoal,
  WellnessSpendCategory,
  saveOnboardingProfile
} from "../lib/onboarding";

type Step = 1 | 2 | 3 | 4 | 5;

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState<Step>(1);

  const [name, setName] = useState("");
  const [ageRange, setAgeRange] = useState("");
  const [primaryGoal, setPrimaryGoal] = useState<PrimaryGoal>("Energy");

  const [tracksCycle, setTracksCycle] = useState<"Yes" | "Sometimes" | "No">(
    "Sometimes"
  );
  const [currentPhase, setCurrentPhase] = useState<
    "Follicular" | "Ovulatory" | "Luteal" | "Menstrual" | "Not sure"
  >("Not sure");

  const [wellnessSpending, setWellnessSpending] = useState<
    WellnessSpendCategory[]
  >([]);
  const [monthlyBudget, setMonthlyBudget] = useState<number>(200);

  const [sleepHours, setSleepHours] = useState<number>(7);
  const [exerciseDays, setExerciseDays] = useState<number>(3);
  const [stressLevel, setStressLevel] = useState<number>(6);
  const [energyDrain, setEnergyDrain] = useState<EnergyDrainOption>(
    "Busy Schedule"
  );

  const [aiPersona, setAiPersona] =
    useState<AiPersonaOption>("Supportive Coach");

  const toggleSpendingCategory = (category: WellnessSpendCategory) => {
    setWellnessSpending((prev) =>
      prev.includes(category)
        ? prev.filter((c) => c !== category)
        : [...prev, category]
    );
  };

  const goNext = () => {
    setStep((prev) => (prev < 5 ? ((prev + 1) as Step) : prev));
  };

  const goBack = () => {
    setStep((prev) => (prev > 1 ? ((prev - 1) as Step) : prev));
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    saveOnboardingProfile({
      name: name.trim() || "Friend",
      ageRange: ageRange || "Not shared",
      primaryGoal,
      tracksCycle,
      currentPhase,
      wellnessSpending,
      monthlyBudget,
      sleepHours,
      exerciseDays,
      stressLevel,
      energyDrain,
      aiPersona
    });

    router.push("/profile");
  };

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <div className="space-y-2 text-center">
        <p className="pill mx-auto text-[11px]">
          5 quick steps · ~2 minutes
        </p>
        <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          Let&apos;s personalize your FemAI Advisor
        </h1>
        <p className="text-sm text-slate-600 sm:text-base">
          Answer a few gentle questions so your AI coach can tailor guidance to
          your energy, hormones, habits, and money.
        </p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="glass-card space-y-6 p-6 sm:p-7"
      >
        <div className="flex items-center justify-between text-xs text-slate-500">
          <span>Step {step} of 5</span>
          <div className="flex gap-1">
            {[1, 2, 3, 4, 5].map((s) => (
              <span
                key={s}
                className={`h-1.5 w-6 rounded-full ${
                  s <= step ? "bg-lavender-500" : "bg-lavender-100"
                }`}
              />
            ))}
          </div>
        </div>

        {step === 1 && (
          <section className="space-y-5">
            <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
              Step 1 · Identity
            </h2>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="space-y-2">
                <label className="text-xs font-medium text-slate-700">
                  Name
                </label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="How should FemAI address you?"
                  className="w-full rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2.5 text-sm text-slate-900 shadow-sm outline-none focus:ring-2 focus:ring-lavender-400"
                />
              </div>
              <div className="space-y-2">
                <label className="text-xs font-medium text-slate-700">
                  Age range
                </label>
                <select
                  value={ageRange}
                  onChange={(e) => setAgeRange(e.target.value)}
                  className="w-full rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2.5 text-sm text-slate-900 shadow-sm outline-none focus:ring-2 focus:ring-lavender-400"
                >
                  <option value="">Prefer not to say</option>
                  <option value="18–24">18–24</option>
                  <option value="25–34">25–34</option>
                  <option value="35–44">35–44</option>
                  <option value="45–54">45–54</option>
                  <option value="55+">55+</option>
                </select>
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                What do you want to improve most right now?
              </label>
              <div className="grid gap-2 sm:grid-cols-3">
                {[
                  "Energy",
                  "Hormone Balance",
                  "Fitness Consistency",
                  "Stress Management",
                  "Saving Money",
                  "Wellness Budgeting"
                ].map((goal) => (
                  <button
                    key={goal}
                    type="button"
                    onClick={() =>
                      setPrimaryGoal(goal as PrimaryGoal)
                    }
                    className={`rounded-2xl border px-3 py-2 text-xs font-medium transition ${
                      primaryGoal === goal
                        ? "border-lavender-500 bg-lavender-50 text-lavender-700"
                        : "border-slate-200 bg-white/80 text-slate-700 hover:border-lavender-200"
                    }`}
                  >
                    {goal}
                  </button>
                ))}
              </div>
            </div>
          </section>
        )}

        {step === 2 && (
          <section className="space-y-5">
            <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
              Step 2 · Cycle awareness
            </h2>
            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Do you track your menstrual cycle?
              </label>
              <div className="flex flex-wrap gap-2">
                {["Yes", "Sometimes", "No"].map((option) => (
                  <button
                    key={option}
                    type="button"
                    onClick={() =>
                      setTracksCycle(option as "Yes" | "Sometimes" | "No")
                    }
                    className={`rounded-full px-4 py-2 text-xs font-medium transition ${
                      tracksCycle === option
                        ? "bg-lavender-600 text-white shadow-md"
                        : "bg-white/80 text-slate-700 shadow-sm hover:bg-lavender-50"
                    }`}
                  >
                    {option}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Where are you in your cycle right now?
              </label>
              <div className="grid gap-2 sm:grid-cols-3">
                {[
                  "Follicular",
                  "Ovulatory",
                  "Luteal",
                  "Menstrual",
                  "Not sure"
                ].map((phase) => (
                  <button
                    key={phase}
                    type="button"
                    onClick={() =>
                      setCurrentPhase(
                        phase as
                          | "Follicular"
                          | "Ovulatory"
                          | "Luteal"
                          | "Menstrual"
                          | "Not sure"
                      )
                    }
                    className={`rounded-2xl border px-3 py-2 text-xs font-medium transition ${
                      currentPhase === phase
                        ? "border-lavender-500 bg-lavender-50 text-lavender-700"
                        : "border-slate-200 bg-white/80 text-slate-700 hover:border-lavender-200"
                    }`}
                  >
                    {phase}
                  </button>
                ))}
              </div>
            </div>
          </section>
        )}

        {step === 3 && (
          <section className="space-y-5">
            <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
              Step 3 · Wellness spending
            </h2>
            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Where do you currently spend on wellness? (Select all that fit)
              </label>
              <div className="grid gap-2 sm:grid-cols-3">
                {[
                  "Gym/Fitness",
                  "Supplements",
                  "Skincare",
                  "Therapy/Mental Health",
                  "Healthy Food",
                  "Wellness Apps",
                  "None yet"
                ].map((cat) => {
                  const isActive = wellnessSpending.includes(
                    cat as WellnessSpendCategory
                  );
                  return (
                    <button
                      key={cat}
                      type="button"
                      onClick={() =>
                        toggleSpendingCategory(cat as WellnessSpendCategory)
                      }
                      className={`rounded-2xl border px-3 py-2 text-xs font-medium transition ${
                        isActive
                          ? "border-lavender-500 bg-lavender-50 text-lavender-700"
                          : "border-slate-200 bg-white/80 text-slate-700 hover:border-lavender-200"
                      }`}
                    >
                      {cat}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Monthly wellness budget (USD)
              </label>
              <div className="flex items-center gap-2 rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2.5 shadow-sm">
                <span className="text-xs text-slate-500">$</span>
                <input
                  type="number"
                  min={0}
                  value={Number.isNaN(monthlyBudget) ? "" : monthlyBudget}
                  onChange={(e) =>
                    setMonthlyBudget(parseFloat(e.target.value) || 0)
                  }
                  className="w-full bg-transparent text-sm text-slate-900 outline-none"
                  placeholder="e.g. 200"
                />
              </div>
              <p className="text-[11px] text-slate-500">
                Think of therapy, classes, apps, skincare, supplements, and
                restorative rituals.
              </p>
            </div>
          </section>
        )}

        {step === 4 && (
          <section className="space-y-5">
            <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
              Step 4 · Lifestyle snapshot
            </h2>

            <div className="grid gap-4 sm:grid-cols-2">
              <div className="space-y-2">
                <label className="flex items-center justify-between text-xs font-medium text-slate-700">
                  <span>Sleep hours per night</span>
                  <span className="text-[11px] text-slate-500">
                    {sleepHours} hours
                  </span>
                </label>
                <input
                  type="range"
                  min={0}
                  max={12}
                  step={0.5}
                  value={sleepHours}
                  onChange={(e) => setSleepHours(parseFloat(e.target.value))}
                  className="w-full accent-lavender-500"
                />
              </div>
              <div className="space-y-2">
                <label className="flex items-center justify-between text-xs font-medium text-slate-700">
                  <span>Exercise days per week</span>
                  <span className="text-[11px] text-slate-500">
                    {exerciseDays} days
                  </span>
                </label>
                <input
                  type="range"
                  min={0}
                  max={7}
                  step={1}
                  value={exerciseDays}
                  onChange={(e) =>
                    setExerciseDays(parseInt(e.target.value, 10))
                  }
                  className="w-full accent-lavender-500"
                />
              </div>
            </div>

            <div className="grid gap-4 sm:grid-cols-[1.4fr,1.6fr]">
              <div className="space-y-2">
                <label className="flex items-center justify-between text-xs font-medium text-slate-700">
                  <span>Stress level (1–10)</span>
                  <span className="text-[11px] text-slate-500">
                    {stressLevel}
                  </span>
                </label>
                <input
                  type="range"
                  min={1}
                  max={10}
                  step={1}
                  value={stressLevel}
                  onChange={(e) =>
                    setStressLevel(parseInt(e.target.value, 10))
                  }
                  className="w-full accent-lavender-500"
                />
              </div>
              <div className="space-y-2">
                <label className="text-xs font-medium text-slate-700">
                  What usually drains your energy most?
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    "Work/School",
                    "Hormones",
                    "Poor Sleep",
                    "Stress",
                    "Overthinking",
                    "Busy Schedule"
                  ].map((item) => (
                    <button
                      key={item}
                      type="button"
                      onClick={() =>
                        setEnergyDrain(item as EnergyDrainOption)
                      }
                      className={`rounded-2xl border px-3 py-2 text-[11px] font-medium transition ${
                        energyDrain === item
                          ? "border-lavender-500 bg-lavender-50 text-lavender-700"
                          : "border-slate-200 bg-white/80 text-slate-700 hover:border-lavender-200"
                      }`}
                    >
                      {item}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </section>
        )}

        {step === 5 && (
          <section className="space-y-5">
            <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
              Step 5 · AI persona
            </h2>
            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                How do you want your AI advisor to guide you?
              </label>
              <div className="grid gap-2 sm:grid-cols-2">
                {[
                  "Supportive Coach",
                  "Scientific Explainer",
                  "Motivational Trainer",
                  "Calm Wellness Guide"
                ].map((persona) => (
                  <button
                    key={persona}
                    type="button"
                    onClick={() =>
                      setAiPersona(persona as AiPersonaOption)
                    }
                    className={`rounded-2xl border px-3 py-2 text-xs font-medium transition ${
                      aiPersona === persona
                        ? "border-lavender-500 bg-lavender-50 text-lavender-700"
                        : "border-slate-200 bg-white/80 text-slate-700 hover:border-lavender-200"
                    }`}
                  >
                    {persona}
                  </button>
                ))}
              </div>
              <p className="text-[11px] text-slate-500">
                FemAI will use this tone across chat, tips, and recommendations
                while staying grounded, evidence-informed, and kind.
              </p>
            </div>
          </section>
        )}

        <div className="flex items-center justify-between border-t border-slate-100 pt-4 text-xs">
          <button
            type="button"
            onClick={goBack}
            disabled={step === 1}
            className="secondary-btn disabled:opacity-40"
          >
            Back
          </button>
          {step < 5 ? (
            <button
              type="button"
              onClick={goNext}
              className="primary-btn"
            >
              Next
            </button>
          ) : (
            <button type="submit" className="primary-btn">
              Finish &amp; view profile
            </button>
          )}
        </div>
      </form>
    </div>
  );
}
```

---

## FILE: app/profile/page.tsx

```tsx
"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import {
  OnboardingProfile,
  loadOnboardingProfile
} from "../lib/onboarding";

function deriveArchetype(profile: OnboardingProfile): {
  label: string;
  description: string;
} {
  if (
    profile.primaryGoal === "Hormone Balance" ||
    profile.tracksCycle === "Yes"
  ) {
    return {
      label: "The Hormone Harmonizer",
      description:
        "You're tuning into your hormonal rhythms and looking for aligned habits, not just quick fixes. FemAI will help you pair cycle-aware strategies with everyday life."
    };
  }

  if (
    profile.primaryGoal === "Energy" ||
    profile.energyDrain === "Work/School" ||
    profile.stressLevel >= 7
  ) {
    return {
      label: "The Resilient Achiever",
      description:
        "You carry a lot and still care deeply about your well-being. FemAI will focus on realistic boundaries, recovery, and money moves that protect your energy."
    };
  }

  return {
    label: "The Wellness Explorer",
    description:
      "You're experimenting with what makes you feel grounded, clear, and supported. FemAI will help you test small changes across hormones, habits, and spending."
  };
}

function summarizeProfile(profile: OnboardingProfile): string {
  const parts: string[] = [];

  parts.push(
    `Your primary focus right now is ${profile.primaryGoal.toLowerCase()}.`
  );

  if (profile.currentPhase !== "Not sure") {
    parts.push(
      `You're currently in the ${profile.currentPhase.toLowerCase()} phase, where your body's needs shift across energy, mood, and recovery.`
    );
  }

  parts.push(
    `You're sleeping around ${profile.sleepHours} hours per night and moving about ${profile.exerciseDays} days each week, with stress at about ${profile.stressLevel}/10.`
  );

  if (profile.monthlyBudget > 0) {
    parts.push(
      `You've set a monthly wellness budget of approximately $${Math.round(
        profile.monthlyBudget
      )}, spread across ${profile.wellnessSpending.length > 0 ? "areas like " + profile.wellnessSpending.join(", ") : "future wellness investments"}.`
    );
  }

  parts.push(
    "Your biggest opportunity is creating kinder boundaries around what drains you, protecting sleep, and making sure your wellness spending matches what truly supports your body and mind."
  );

  return parts.join(" ");
}

export default function ProfilePage() {
  const [profile, setProfile] = useState<OnboardingProfile | null>(null);

  useEffect(() => {
    const loaded = loadOnboardingProfile();
    setProfile(loaded);
  }, []);

  if (!profile) {
    return (
      <div className="space-y-4">
        <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          Create your FemAI profile
        </h1>
        <p className="max-w-xl text-sm text-slate-600 sm:text-base">
          We couldn&apos;t find your onboarding details yet. Take 2 minutes to
          answer a few questions and unlock personalized, cycle-aware insights
          across wellness and money.
        </p>
        <Link href="/onboarding" className="primary-btn w-fit">
          Start onboarding
        </Link>
      </div>
    );
  }

  const archetype = deriveArchetype(profile);
  const summary = summarizeProfile(profile);

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="space-y-1">
          <p className="pill text-[11px]">
            Personalized profile · AI tuned to you
          </p>
          <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
            Welcome, {profile.name}.
          </h1>
          <p className="max-w-2xl text-sm text-slate-600 sm:text-base">
            FemAI will use this snapshot to personalize chat responses, daily
            tips, and wellness + finance guidance around your real life.
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <Link href="/dashboard" className="secondary-btn text-xs sm:text-sm">
            Open dashboard
          </Link>
          <Link href="/advisor" className="primary-btn text-xs sm:text-sm">
            Chat with your AI advisor
          </Link>
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-[2.2fr,2fr] lg:items-start">
        <section className="glass-card space-y-4 p-5 sm:p-6">
          <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
            Your wellness &amp; money snapshot
          </h2>
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-1">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Primary goal
              </p>
              <p className="text-sm font-semibold text-slate-900">
                {profile.primaryGoal}
              </p>
              <p className="text-[11px] text-slate-500">
                This is where FemAI will focus first in your guidance.
              </p>
            </div>
            <div className="space-y-1">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Cycle phase
              </p>
              <p className="text-sm font-semibold text-slate-900">
                {profile.currentPhase}
              </p>
              <p className="text-[11px] text-slate-500">
                Tips and simulations on the dashboard will adjust to this phase.
              </p>
            </div>
            <div className="space-y-1">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Wellness budget
              </p>
              <p className="text-sm font-semibold text-slate-900">
                {profile.monthlyBudget > 0
                  ? `$${Math.round(profile.monthlyBudget)} / month`
                  : "Not set yet"}
              </p>
              <p className="text-[11px] text-slate-500">
                Used to shape spending recommendations and financial nudges.
              </p>
            </div>
            <div className="space-y-1">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Stress level
              </p>
              <p className="text-sm font-semibold text-slate-900">
                {profile.stressLevel}/10
              </p>
              <p className="text-[11px] text-slate-500">
                Expect extra focus on nervous system support and boundaries.
              </p>
            </div>
          </div>

          <div className="mt-2 rounded-2xl bg-lavender-50/70 p-4 text-xs text-slate-700">
            <p className="mb-1 text-[11px] font-semibold uppercase tracking-wide text-lavender-700">
              FemAI summary
            </p>
            <p>{summary}</p>
          </div>

          <p className="text-[10px] text-slate-500">
            This profile is for personalization only and does not replace
            medical or financial care. Always consult licensed professionals for
            diagnosis, treatment, or detailed money planning.
          </p>
        </section>

        <section className="space-y-4">
          <div className="glass-card space-y-3 p-5 sm:p-6">
            <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">
              FemAI archetype
            </p>
            <p className="text-lg font-semibold text-lavender-700">
              {archetype.label}
            </p>
            <p className="text-sm text-slate-700">{archetype.description}</p>
          </div>

          <div className="glass-card space-y-3 p-5 sm:p-6">
            <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">
              Future you simulation (soft preview)
            </p>
            <p className="text-sm text-slate-700">
              If you gently protect 1–2 more hours of sleep per week, add one
              movement session, and redirect a small portion of impulse
              spending toward true supports like therapy or nourishing food,
              your future you likely feels more stable across cycles and less
              stressed about money. FemAI will keep suggesting tiny, doable
              shifts—not all-or-nothing overhauls.
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}
```

---

## FILE: app/dashboard/page.tsx

```tsx
"use client";

import { useEffect, useState } from "react";
import {
  OnboardingProfile,
  loadOnboardingProfile
} from "../lib/onboarding";

type CyclePhase = "Follicular" | "Ovulatory" | "Luteal" | "Menstrual";

interface SimulationResult {
  healthScore: number;
  predictedCost: number;
  advice: string;
}

function dailyTip(phase: CyclePhase, profile: OnboardingProfile | null): string {
  const name = profile?.name || "Today";
  const goal = profile?.primaryGoal;

  if (phase === "Follicular") {
    return `${name}, your follicular phase often brings rising energy. Pair that with your goal${
      goal ? ` of ${goal.toLowerCase()}` : ""
    } by scheduling learning, planning, or strength sessions while you naturally feel more open and focused.`;
  }
  if (phase === "Ovulatory") {
    return `Ovulatory days can feel more social and expressive. Use that boost for collaborative work, networking, or movement that feels fun—not punishing—then protect wind-down time at night.`;
  }
  if (phase === "Luteal") {
    return `In your luteal phase, it's normal to feel a bit heavier or more sensitive. Build in buffers between tasks, aim for earlier sleep, and let your movement skew toward walks, Pilates, or yoga.`;
  }
  return `Menstrual days are a natural time for reflection and gentler output. Where possible, clear space for rest, warm foods, and lower-stakes tasks while your body does intense internal work.`;
}

function productivitySuggestion(phase: CyclePhase): string {
  switch (phase) {
    case "Follicular":
      return "Use follicular energy for learning, planning, and starting new projects—your brain is primed for exploration.";
    case "Ovulatory":
      return "Leverage ovulatory confidence for meetings, interviews, presentations, and relationship-centered work.";
    case "Luteal":
      return "The luteal phase is ideal for detail work, editing, organizing, and gently closing open loops.";
    case "Menstrual":
    default:
      return "During your bleed, protect time for reflection, reviewing what's working, and low-pressure admin instead of heavy lifting.";
  }
}

function budgetInsight(
  budget: number,
  profile: OnboardingProfile | null
): string {
  if (!budget || budget <= 0) {
    return "Consider starting with even a tiny wellness line in your budget—like $20–$40 a month you intentionally direct toward what supports you most.";
  }

  const categories = profile?.wellnessSpending || [];
  if (categories.length === 0) {
    return `With roughly $${Math.round(
      budget
    )} per month, you might test a simple split: 40% movement, 30% mental health, and 30% rest-focused comforts like massages, baths, or cozy tools.`;
  }

  if (categories.includes("Therapy/Mental Health")) {
    return `Since therapy or mental health support is in the mix, protect that in your ~$${Math.round(
      budget
    )} budget first, then allocate what's left across movement and everyday comforts rather than impulse buys.`;
  }

  return `With a wellness budget of about $${Math.round(
    budget
  )}, choose 1–2 "non-negotiable" supports from your current spending and gently trim the rest so your money matches what truly moves the needle.`;
}

export default function DashboardPage() {
  const [profile, setProfile] = useState<OnboardingProfile | null>(null);
  const [phase, setPhase] = useState<CyclePhase>("Follicular");
  const [sleepHours, setSleepHours] = useState<number>(7);
  const [exerciseDays, setExerciseDays] = useState<number>(3);
  const [budget, setBudget] = useState<number>(200);
  const [result, setResult] = useState<SimulationResult | null>(null);

  useEffect(() => {
    const loaded = loadOnboardingProfile();
    if (!loaded) return;

    setProfile(loaded);
    if (
      loaded.currentPhase === "Follicular" ||
      loaded.currentPhase === "Ovulatory" ||
      loaded.currentPhase === "Luteal" ||
      loaded.currentPhase === "Menstrual"
    ) {
      setPhase(loaded.currentPhase);
    }
    if (loaded.sleepHours) setSleepHours(loaded.sleepHours);
    if (loaded.exerciseDays) setExerciseDays(loaded.exerciseDays);
    if (loaded.monthlyBudget) setBudget(loaded.monthlyBudget);
  }, []);

  const runSimulation = () => {
    let score = 75;

    if (sleepHours <= 3) {
      score -= 30;
    } else if (sleepHours <= 5) {
      score -= 18;
    } else if (sleepHours < 7) {
      score -= 8;
    } else if (sleepHours >= 7 && sleepHours <= 9) {
      score += 5;
    }

    if ((phase === "Luteal" || phase === "Menstrual") && sleepHours < 6) {
      score -= 8;
    }

    if (exerciseDays === 0) {
      score -= 20;
    } else if (exerciseDays <= 2) {
      score -= 8;
    } else if (exerciseDays <= 4) {
      score += 2;
    } else {
      score += 6;
    }

    const healthScore = Math.max(0, Math.min(100, Math.round(score)));

    const baseline = budget || 0;
    let predictedCost = baseline;

    if (healthScore < 30) {
      predictedCost += 200;
    } else if (healthScore < 50) {
      predictedCost += 120;
    } else if (healthScore < 70) {
      predictedCost += 60;
    } else if (healthScore > 85) {
      predictedCost -= 40;
    }

    predictedCost = Math.max(0, Math.round(predictedCost));

    const adviceParts: string[] = [];

    if (healthScore < 30) {
      adviceParts.push(
        "Right now your simulated wellness score is quite low, which suggests your body and nervous system are under a lot of strain. This isn't about blame—it's a signal to introduce the smallest, kindest changes possible."
      );
    } else if (healthScore < 50) {
      adviceParts.push(
        "Your simulated wellness score is on the lower side, meaning there's real opportunity to feel better with gentle, consistent shifts in sleep, movement, and stress support."
      );
    } else if (healthScore < 70) {
      adviceParts.push(
        "Your simulated wellness score is moderate. Some foundations are there, and small upgrades in rest and routine could move the needle meaningfully."
      );
    } else {
      adviceParts.push(
        "Your simulated wellness score is relatively strong. The goal now is to keep things sustainable and aligned with your cycle, rather than chasing perfection."
      );
    }

    if (phase === "Follicular") {
      adviceParts.push(
        "You are in your follicular phase—energy often starts to build. This is a great window for strength training, planning, and creative work."
      );
    } else if (phase === "Ovulatory") {
      adviceParts.push(
        "You are in your ovulatory phase—social energy and confidence can feel higher. Consider scheduling collaborative work, networking, or high-intensity workouts if they feel good."
      );
    } else if (phase === "Luteal") {
      adviceParts.push(
        "You are in your luteal phase—your body is preparing to bleed. Prioritize calming routines, nourishing meals, and earlier bedtimes to support mood and energy."
      );
    } else if (phase === "Menstrual") {
      adviceParts.push(
        "You are in your menstrual phase—rest, reflection, and gentle movement are especially supportive. Give yourself permission to slow down where you can."
      );
    }

    if (sleepHours <= 3) {
      adviceParts.push(
        "Sleep looks extremely short right now. If it's within your control, prioritise adding even 30–60 minutes of rest at a time, and consider speaking with a clinician if this pattern continues."
      );
    } else if (sleepHours < 7) {
      adviceParts.push(
        "Aim for a consistent 7–9 hours of sleep. Try winding down 30 minutes earlier, dimming lights, and stepping away from screens before bed."
      );
    } else {
      adviceParts.push(
        "Your sleep looks broadly supportive—keep protecting your wind-down routine and morning light exposure to stabilize energy and mood."
      );
    }

    if (exerciseDays === 0) {
      adviceParts.push(
        "Movement is essentially at zero right now. Start with very small, kind goals—like a 10-minute walk most days or stretching while you watch a show. Consistency matters more than intensity."
      );
    } else if (exerciseDays <= 2) {
      adviceParts.push(
        "You are moving a bit each week already. See if you can add one more low-pressure session, like gentle yoga or a walk with a friend."
      );
    } else {
      adviceParts.push(
        "Your movement routine is a strong foundation. Check in with how your training lines up with each phase—higher intensity in follicular/ovulatory and softer movement in luteal/menstrual can feel more sustainable."
      );
    }

    if (!budget || budget <= 0) {
      adviceParts.push(
        "Consider setting aside even a small monthly wellness amount—this could go toward therapy co-pays, a fitness class you love, or a calming ritual at home."
      );
    } else if (predictedCost > budget) {
      adviceParts.push(
        "Your predicted wellness expenses may sit above your current budget. You might prioritize 1–2 high-impact supports (like therapy or a class you truly enjoy) and pause lower-impact impulse purchases."
      );
    } else {
      adviceParts.push(
        "Your current budget looks aligned with your projected needs. Keep tracking where it actually goes—toward things that genuinely support your energy, mood, and long-term health."
      );
    }

    adviceParts.push(
      "This simulation is informational only and not medical or financial advice. Always partner with healthcare and financial professionals for personalized care."
    );

    setResult({
      healthScore,
      predictedCost,
      advice: adviceParts.join(" ")
    });
  };

  return (
    <div className="space-y-8">
      <div className="space-y-3">
        <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          Wellness &amp; Finance Dashboard
        </h1>
        <p className="max-w-2xl text-sm text-slate-600 sm:text-base">
          Input your current phase, habits, and wellness budget. FemAI will
          simulate a holistic health score, estimate wellness spending, and
          share gentle, cycle-aware recommendations.
        </p>
      </div>

      <div className="grid gap-6 lg:grid-cols-[3fr,2.2fr] lg:items-start">
        <section className="glass-card space-y-6 p-6">
          <h2 className="text-sm font-semibold text-slate-900 sm:text-base">
            Your current snapshot
          </h2>

          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Cycle phase
              </label>
              <select
                value={phase}
                onChange={(e) => setPhase(e.target.value as CyclePhase)}
                className="w-full rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2.5 text-sm text-slate-900 shadow-sm focus:outline-none focus:ring-2 focus:ring-lavender-400"
              >
                <option value="Follicular">Follicular</option>
                <option value="Ovulatory">Ovulatory</option>
                <option value="Luteal">Luteal</option>
                <option value="Menstrual">Menstrual</option>
              </select>
              <p className="text-[11px] text-slate-500">
                Align habits and spending with how your hormones fluctuate
                through each phase.
              </p>
            </div>

            <div className="space-y-2">
              <label className="flex items-center justify-between text-xs font-medium text-slate-700">
                <span>Sleep per night</span>
                <span className="text-[11px] text-slate-500">
                  {sleepHours} hours
                </span>
              </label>
              <input
                type="range"
                min={0}
                max={12}
                step={0.5}
                value={sleepHours}
                onChange={(e) => setSleepHours(parseFloat(e.target.value))}
                className="w-full accent-lavender-500"
              />
              <p className="text-[11px] text-slate-500">
                Aim for 7–9 hours, especially in luteal and menstrual phases.
              </p>
            </div>

            <div className="space-y-2">
              <label className="flex items-center justify-between text-xs font-medium text-slate-700">
                <span>Exercise days per week</span>
                <span className="text-[11px] text-slate-500">
                  {exerciseDays} days
                </span>
              </label>
              <input
                type="range"
                min={0}
                max={7}
                step={1}
                value={exerciseDays}
                onChange={(e) => setExerciseDays(parseInt(e.target.value, 10))}
                className="w-full accent-lavender-500"
              />
              <p className="text-[11px] text-slate-500">
                Think in terms of small, repeatable movement rather than
                perfection.
              </p>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium text-slate-700">
                Monthly wellness budget (USD)
              </label>
              <div className="flex items-center gap-2 rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2.5 shadow-sm">
                <span className="text-xs text-slate-500">$</span>
                <input
                  type="number"
                  min={0}
                  value={Number.isNaN(budget) ? "" : budget}
                  onChange={(e) => setBudget(parseFloat(e.target.value) || 0)}
                  className="w-full bg-transparent text-sm text-slate-900 outline-none"
                  placeholder="e.g. 200"
                />
              </div>
              <p className="text-[11px] text-slate-500">
                Include therapy, coaching, classes, supplements, and
                restorative self-care.
              </p>
            </div>
          </div>

          <div className="flex flex-wrap items-center justify-between gap-3 border-t border-slate-100 pt-4">
            <p className="text-[11px] text-slate-500">
              This is a gentle simulation, not medical or financial advice.
            </p>
            <button
              type="button"
              onClick={runSimulation}
              className="primary-btn text-xs sm:text-sm"
            >
              Run simulation
            </button>
          </div>
        </section>

        <section className="space-y-4">
          <div className="glass-card grid gap-4 p-5 sm:grid-cols-3">
            <div className="space-y-1 border-r border-slate-100 pr-3 sm:pr-4">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Health score
              </p>
              <p className="text-3xl font-semibold text-lavender-700">
                {result ? result.healthScore : "—"}
              </p>
              <p className="text-[11px] text-slate-500">
                Higher scores reflect more supportive sleep, movement, and
                alignment with your phase.
              </p>
            </div>

            <div className="space-y-1 border-r border-slate-100 px-3 sm:px-4">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Predicted monthly wellness cost
              </p>
              <p className="text-2xl font-semibold text-slate-900">
                {result ? `$${result.predictedCost}` : "—"}
              </p>
              <p className="text-[11px] text-slate-500">
                Includes additional care needs when your body may need more
                support.
              </p>
            </div>

            <div className="space-y-1 pl-3 sm:pl-4">
              <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">
                Phase
              </p>
              <p className="text-sm font-semibold text-slate-900">{phase}</p>
              <p className="text-[11px] text-slate-500">
                Use this insight alongside your own body wisdom—not instead of
                it.
              </p>
            </div>
          </div>

          <div className="glass-card h-56 max-h-72 overflow-y-auto p-5">
            <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
              AI wellness recommendation
            </p>
            <p className="mt-3 text-sm text-slate-700">
              {result
                ? result.advice
                : "Run a simulation to receive phase-aware guidance on your habits, energy, and wellness spending."}
            </p>
          </div>

          <div className="grid gap-4 lg:grid-cols-2">
            <div className="glass-card space-y-2 p-4">
              <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">
                Daily AI tip
              </p>
              <p className="text-sm text-slate-700">
                {dailyTip(phase, profile)}
              </p>
            </div>
            <div className="glass-card space-y-2 p-4">
              <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">
                Cycle-aware productivity
              </p>
              <p className="text-sm text-slate-700">
                {productivitySuggestion(phase)}
              </p>
            </div>
          </div>

          <div className="glass-card space-y-2 p-4">
            <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">
              Wellness + finance insight
            </p>
            <p className="text-sm text-slate-700">
              {budgetInsight(budget, profile)}
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}
```

---

## FILE: app/advisor/page.tsx

```tsx
"use client";

import { FormEvent, useEffect, useState } from "react";
import {
  AiPersonaOption,
  OnboardingProfile,
  loadOnboardingProfile
} from "../lib/onboarding";

type Role = "user" | "ai";

interface ChatMessage {
  id: number;
  role: Role;
  content: string;
}

function describeTone(aiPersona?: AiPersonaOption): string {
  switch (aiPersona) {
    case "Scientific Explainer":
      return "grounded and science-informed";
    case "Motivational Trainer":
      return "upbeat and accountability-focused";
    case "Calm Wellness Guide":
      return "slow, soothing, and nervous-system aware";
    case "Supportive Coach":
    default:
      return "gentle, encouraging, and practical";
  }
}

function getAiResponse(
  input: string,
  profile: OnboardingProfile | null
): string {
  const text = input.toLowerCase();
  const name = profile?.name || "friend";
  const goal = profile?.primaryGoal || "balancing your energy, hormones, and money";
  const phase = profile?.currentPhase;
  const budget = profile?.monthlyBudget;
  const tone = describeTone(profile?.aiPersona);

  if (
    ["hi", "hey", "hello"].some((greeting) => text.startsWith(greeting)) ||
    text.includes("how are you") ||
    text.includes("hows your day") ||
    text.includes("how's your day")
  ) {
    return `Hi ${name}, thanks for checking in with me. I'm here as your ${tone} FemAI Advisor, focused on ${goal.toLowerCase()}. You can ask me about your current phase, symptoms, sleep, stress, workouts, or how to spend your wellness budget in a way that actually supports your body and future self. What feels most important to explore together right now?`;
  }

  if (text.includes("pregnancy")) {
    return "Thank you for sharing that you're thinking about pregnancy. It's a powerful season that benefits from both medical support and nurturing routines. Focus on a gentle, colorful diet, consistent sleep, and stress-reducing rituals like short walks, breathwork, or journaling. It's also wise to speak with a healthcare provider about preconception labs, supplements (like prenatal vitamins), and any medications. Financially, you might begin a small monthly savings bucket for prenatal care, time off work, and baby essentials—even $25–$50 per month adds up over time.";
  }

  if (text.includes("menopause") || text.includes("perimenopause")) {
    return "Menopause and perimenopause can bring shifts in sleep, mood, temperature, and body composition—and it's completely valid to want extra support. Tracking symptoms, sleep, and energy can help you notice patterns to discuss with your clinician. Strength training, protein-rich meals, and stress management are especially supportive in this chapter. Financially, consider budgeting for hormone-informed care, therapy, and movement practices that help you feel grounded, like yoga or strength classes.";
  }

  if (text.includes("period") || text.includes("cramp")) {
    return "Period symptoms like cramps, fatigue, and mood changes are common, but you still deserve comfort and care. Gentle movement, warmth (like a heating pad), magnesium-rich foods, and anti-inflammatory meals can ease discomfort for many people. If your pain is severe or interfering with daily life, please talk with a healthcare provider to rule out conditions like endometriosis or fibroids. From a budget perspective, you might set aside a small monthly amount for high-quality menstrual products, pain relief tools, or supportive appointments.";
  }

  if (
    text.includes("sleep") ||
    text.includes("insomnia") ||
    text.includes("tired")
  ) {
    const phaseNote =
      phase === "Luteal" || phase === "Menstrual"
        ? "Because you mentioned you may be in a lower-energy phase, even a 20–30 minute earlier wind-down could noticeably soften symptoms."
        : "Even outside your bleed, your nervous system loves rhythm—consistent bed and wake times are a quiet superpower.";
    return `Sleep is one of the most powerful wellness levers—especially around the luteal and menstrual phases. Start with a consistent wake time, gentle evening wind-down (dim lights, fewer screens, calming tea), and a short transition ritual like stretching or reading. ${phaseNote} If poor sleep persists or feels extreme, check in with a clinician. Financially, prioritize low-cost supports first—like a sleep mask or blackout curtains—before investing in higher-ticket gadgets.`;
  }

  if (text.includes("stress") || text.includes("burnout") || text.includes("anxiety")) {
    return "Chronic stress and burnout can quietly drain both your energy and your finances. Start by building micro-moments of regulation into your day: 3 deep breaths before meetings, short walks between tasks, or 5 minutes of stretching when you close your laptop. If you can, protect at least one evening per week as a non-negotiable rest block. In your budget, consider shifting a small amount toward therapy, coaching, or calming practices that genuinely help you reset, even if that means pausing lower-impact expenses for a season.";
  }

  if (text.includes("exercise") || text.includes("workout") || text.includes("movement")) {
    return "When it comes to movement, consistency beats intensity—especially across the menstrual cycle. In follicular and ovulatory phases, many people feel best with more energizing workouts like strength training or intervals. In luteal and menstrual phases, your body may prefer walking, Pilates, or yoga. Choose forms of movement that feel kind rather than punishing. Budget-wise, you don't need an expensive membership to benefit—start with walks, bodyweight strength at home, or affordable community classes, and upgrade only if it truly adds value for you.";
  }

  if (
    text.includes("budget") ||
    text.includes("money") ||
    text.includes("spend") ||
    text.includes("spending")
  ) {
    const budgetLine =
      budget && budget > 0
        ? `Since you mentioned a wellness budget around $${Math.round(
            budget
          )}, we can treat that as a container instead of a limit—decide what percentage goes to therapy, movement, food, or rest.`
        : "You don't need a huge budget to start—simply noticing where your current wellness dollars go is a powerful first step.";
    return `A wellness budget works best when it's intentional, not perfect. Begin by listing your current wellness-related expenses—therapy, fitness, supplements, apps, beauty, and self-care. Highlight which ones meaningfully improve your physical or mental health, and which feel more like impulse buys. Aim to protect the high-impact items and gradually trim or pause the rest. ${budgetLine} Even redirecting $30–$50 a month from low-impact spending to savings, debt payoff, or therapy can create more long-term ease.`;
  }

  if (text.includes("saving") || text.includes("savings") || text.includes("emergency")) {
    return "Building savings for wellness and life emergencies is an act of self-care. Start with a small, realistic target—like one month of essential expenses over time—and automate a transfer on payday, even if it's a modest amount. You can also create a dedicated 'wellness sinking fund' for therapy, medical visits, or retreat-style rest, so those costs feel planned rather than stressful. If cash flow is tight, look for 1–2 small recurring expenses you can gently reduce and redirect into savings instead.";
  }

  if (text.includes("invest") || text.includes("investing")) {
    return "Investing is about aligning your money with your future energy and needs. Before investing, it's helpful to have some emergency savings and a basic handle on debt and monthly cash flow. Many people start with employer retirement accounts or broad, low-fee index funds, and they invest consistently over time instead of trying to time the market. While this app can't give personalized investment advice, exploring educational resources and, if possible, a fee-only advisor can help you build a plan that supports your long-term wellness goals.";
  }

  if (text.includes("debt") || text.includes("credit card")) {
    return "Debt can feel heavy, especially when you also want to spend on wellness. Start by listing your debts, minimum payments, and interest rates. Focus on making at least the minimums while choosing one balance to pay extra toward, even by a small amount. At the same time, protect a tiny wellness line in your budget—like $10–$20 a month for something that genuinely supports your body or mind—so your plan feels sustainable instead of depriving.";
  }

  return `Thank you for sharing that, ${name}. I might not be able to talk about every topic in depth, but I can absolutely help you explore how your hormones, sleep, movement, stress, and money habits are shaping the way you feel day to day. If you'd like, you can tell me where you are in your cycle, how you're sleeping, or what's feeling hard in your body or budget, and I'll offer ${tone} suggestions from there. This space is here to support you holistically, but it isn't a substitute for medical or financial advice.`;
}

export default function AdvisorPage() {
  const [profile, setProfile] = useState<OnboardingProfile | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [nextId, setNextId] = useState(1);

  useEffect(() => {
    const loaded = loadOnboardingProfile();
    setProfile(loaded);

    const name = loaded?.name || "friend";
    const goal =
      loaded?.primaryGoal ||
      "supporting your energy, hormones, habits, and money";
    const tone = describeTone(loaded?.aiPersona);

    setMessages([
      {
        id: 0,
        role: "ai",
        content:
          `Hi ${name}, I'm your FemAI Advisor. I specialize in women's health, hormones, fitness habits, sleep, stress, and money—and I'll keep my tone ${tone}. ` +
          `From what I know so far, I'm here to focus on ${goal.toLowerCase()}. What would you like guidance on today?`
      }
    ]);
    setNextId(1);
  }, []);

  const handleSend = (e: FormEvent) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed) return;

    const userMessage: ChatMessage = {
      id: nextId,
      role: "user",
      content: trimmed
    };
    const aiMessage: ChatMessage = {
      id: nextId + 1,
      role: "ai",
      content: getAiResponse(trimmed, profile)
    };

    setMessages((prev) => [...prev, userMessage, aiMessage]);
    setNextId((id) => id + 2);
    setInput("");
  };

  return (
    <div className="space-y-6">
      <div className="space-y-3">
        <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          AI Wellness &amp; Money Advisor
        </h1>
        <p className="max-w-2xl text-sm text-slate-600 sm:text-base">
          Ask about your cycle, symptoms, movement, sleep, stress, budgeting, or
          wellness spending. You&apos;ll receive warm, practical guidance—not
          judgment. This is educational support only, not medical or financial
          advice.
        </p>
      </div>

      <section className="glass-card flex h-[70vh] max-h-[620px] flex-col p-4 sm:p-6">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <div>
            <p className="text-xs font-semibold text-slate-900">
              FemAI Chat Coach
            </p>
            <p className="text-[11px] text-slate-500">
              Specialized in women&apos;s health, hormones, and money.
            </p>
          </div>
          <span className="pill text-[11px]">
            <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
            AI online
          </span>
        </div>

        <div className="mt-3 flex-1 space-y-3 overflow-y-auto pr-1">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${
                message.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[80%] rounded-2xl px-3 py-2.5 text-xs sm:text-sm ${
                  message.role === "user"
                    ? "bg-gradient-to-br from-lavender-500 to-blush-400 text-white shadow-md"
                    : "bg-white/90 text-slate-800 shadow-sm"
                }`}
              >
                {message.content}
              </div>
            </div>
          ))}
        </div>

        <form
          onSubmit={handleSend}
          className="mt-3 space-y-2 border-t border-slate-100 pt-3"
        >
          <div className="flex items-end gap-2">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about exercise during your luteal phase, how to budget for therapy, or ways to sleep better before your period..."
              className="min-h-[60px] flex-1 resize-none rounded-2xl border border-lavender-100 bg-white/80 px-3 py-2 text-xs text-slate-900 shadow-sm outline-none placeholder:text-slate-400 focus:ring-2 focus:ring-lavender-400"
            />
            <button
              type="submit"
              className="primary-btn h-[60px] px-4 text-xs sm:px-5 sm:text-sm"
            >
              Send
            </button>
          </div>
          <p className="text-[10px] text-slate-500">
            FemAI Advisor can offer education and suggestions, but it does not
            replace care from licensed medical or financial professionals.
          </p>
        </form>
      </section>
    </div>
  );
}
