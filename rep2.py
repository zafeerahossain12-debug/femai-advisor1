## Root config files

### `package.json`

```json
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

### `tsconfig.json`

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

### `next-env.d.ts`

```ts
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
```

### `next.config.mjs`

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

### `postcss.config.mjs`

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
};
```

### `tailwind.config.ts`

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

### `.gitignore`

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

## App styles and layout

### `app/globals.css`

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

### `app/layout.tsx`

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

## Pages

### `app/page.tsx` (Home / Landing)

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

### `app/lib/onboarding.ts`

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

### `app/onboarding/page.tsx`

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

### `app/profile/page.tsx`

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

### `app/dashboard/page.tsx`

Open `app/dashboard/page.tsx` in your project and copy its full contents (418 lines). It contains: state for profile, phase, sleep, exercise, budget, result; `dailyTip`, `productivitySuggestion`, `budgetInsight`; `runSimulation` (score 0–100, predicted cost, advice); and the JSX for inputs, result cards, daily tip, productivity, and budget insight.

---

### `app/advisor/page.tsx`

Open `app/advisor/page.tsx` in your project and copy its full contents (227 lines). It contains: `describeTone`, `getAiResponse(input, profile)` (greetings + keyword responses + default), chat state, and the chat UI with messages and send form.

---

## File tree (source only)

```
femai-advisor/
├── .gitignore
├── package.json
├── tsconfig.json
├── next-env.d.ts
├── next.config.mjs
├── postcss.config.mjs
├── tailwind.config.ts
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   ├── page.tsx
│   ├── lib/
│   │   └── onboarding.ts
│   ├── onboarding/
│   │   └── page.tsx
│   ├── profile/
│   │   └── page.tsx
│   ├── dashboard/
│   │   └── page.tsx
│   └── advisor/
│       └── page.tsx
└── FEMAI_ADVISOR_FULL_SOURCE.md  (this file)
```

---

## Quick start

1. Create a folder (e.g. `femai-advisor`) and add the root config files above.
2. Create `app/`, `app/lib/`, `app/onboarding/`, `app/profile/`, `app/dashboard/`, `app/advisor/`.
3. Copy the contents from your existing repo (or from the full file contents above) into:
   - `app/globals.css`
   - `app/layout.tsx`
   - `app/page.tsx`
   - `app/lib/onboarding.ts`
   - `app/onboarding/page.tsx`
   - `app/profile/page.tsx`
   - `app/dashboard/page.tsx`
   - `app/advisor/page.tsx`
4. Run: `npm install` then `npm run dev`.

The three long page components (`onboarding`, `profile`, `dashboard`, `advisor`) are in your project at the paths listed; this doc gives the exact content for the shorter files and the structure so you can replicate the app anywhere.
