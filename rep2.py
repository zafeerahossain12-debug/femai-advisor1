"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";

// -------------------- TYPES --------------------
type OnboardingProfile = {
  name: string;
  primaryGoal: string;
  currentPhase: string;
  sleepHours: number;
  exerciseDays: number;
  monthlyBudget: number;
  wellnessSpending: string[];
  aiPersona: string;
  energyDrain: string;
  stressLevel: number;
};

type AiPersonaOption =
  | "Supportive Coach"
  | "Scientific Explainer"
  | "Motivational Trainer"
  | "Calm Wellness Guide";

// -------------------- DEFAULT PROFILE --------------------
const defaultProfile: OnboardingProfile = {
  name: "Friend",
  primaryGoal: "Balancing energy, hormones, and money",
  currentPhase: "Follicular",
  sleepHours: 7,
  exerciseDays: 3,
  monthlyBudget: 200,
  wellnessSpending: [],
  aiPersona: "Supportive Coach",
  energyDrain: "",
  stressLevel: 5,
};

// -------------------- UTILS --------------------
function deriveArchetype(profile: OnboardingProfile) {
  if (
    profile.primaryGoal === "Energy" ||
    profile.energyDrain === "Work/School" ||
    profile.stressLevel >= 7
  ) {
    return {
      label: "The Resilient Achiever",
      description:
        "You carry a lot and still care deeply about your well-being. FemAI will focus on realistic boundaries, recovery, and money moves that protect your energy.",
    };
  }

  return {
    label: "The Wellness Explorer",
    description:
      "You're experimenting with what makes you feel grounded, clear, and supported. FemAI will help you test small changes across hormones, habits, and spending.",
  };
}

function summarizeProfile(profile: OnboardingProfile) {
  const parts: string[] = [];
  parts.push(`Your primary focus right now is ${profile.primaryGoal.toLowerCase()}.`);
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
      )}, spread across ${
        profile.wellnessSpending.length > 0
          ? "areas like " + profile.wellnessSpending.join(", ")
          : "future wellness investments"
      }.`
    );
  }
  parts.push(
    "Your biggest opportunity is creating kinder boundaries around what drains you, protecting sleep, and making sure your wellness spending matches what truly supports your body and mind."
  );
  return parts.join(" ");
}

function dailyTip(phase: string, profile: OnboardingProfile | null) {
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
  return `Menstrual days are a natural time for reflection and gentler output. Clear space for rest, warm foods, and lower-stakes tasks while your body does intense internal work.`;
}

function productivitySuggestion(phase: string) {
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

function budgetInsight(budget: number, profile: OnboardingProfile | null) {
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

function describeTone(aiPersona?: AiPersonaOption) {
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

// -------------------- CARD COMPONENT --------------------
const Card: React.FC<{
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
  className?: string;
}> = ({ title, subtitle, children, className = "" }) => (
  <div className={`glass-card space-y-2 p-4 sm:p-6 ${className}`}>
    {title && <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">{title}</p>}
    {subtitle && <p className="text-sm text-slate-700">{subtitle}</p>}
    {children}
  </div>
);

// -------------------- MAIN APP --------------------
export default function App() {
  const [profile, setProfile] = useState<OnboardingProfile | null>(null);

  useEffect(() => {
    // simulate loading onboarding profile
    setTimeout(() => setProfile(defaultProfile), 200);
  }, []);

  if (!profile) {
    return (
      <div className="space-y-4 p-6">
        <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          Create your FemAI profile
        </h1>
        <p className="max-w-xl text-sm text-slate-600 sm:text-base">
          We couldn't find your onboarding details yet. Take 2 minutes to answer a few questions and unlock personalized, cycle-aware insights across wellness and money.
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
    <div className="space-y-6 p-6">
      {/* --- Header --- */}
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="space-y-1">
          <p className="pill text-[11px]">Personalized profile · AI tuned to you</p>
          <h1 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
            Welcome, {profile.name}.
          </h1>
          <p className="max-w-2xl text-sm text-slate-600 sm:text-base">
            FemAI will use this snapshot to personalize chat responses, daily tips, and wellness + finance guidance around your real life.
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

      {/* --- Cards Grid --- */}
      <div className="grid gap-6 lg:grid-cols-[2.2fr,2fr] lg:items-start">
        {/* Left Column */}
        <section className="space-y-4">
          <Card title="Your wellness & money snapshot">
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="space-y-1">
                <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">Primary goal</p>
                <p className="text-sm font-semibold text-slate-900">{profile.primaryGoal}</p>
              </div>
              <div className="space-y-1">
                <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">Cycle phase</p>
                <p className="text-sm font-semibold text-slate-900">{profile.currentPhase}</p>
              </div>
              <div className="space-y-1">
                <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">Wellness budget</p>
                <p className="text-sm font-semibold text-slate-900">
                  {profile.monthlyBudget > 0 ? `$${Math.round(profile.monthlyBudget)} / month` : "Not set yet"}
                </p>
              </div>
              <div className="space-y-1">
                <p className="text-[11px] font-medium uppercase tracking-wide text-slate-500">Stress level</p>
                <p className="text-sm font-semibold text-slate-900">{profile.stressLevel}/10</p>
              </div>
            </div>
            <div className="mt-2 rounded-2xl bg-lavender-50/70 p-4 text-xs text-slate-700">
              <p className="mb-1 text-[11px] font-semibold uppercase tracking-wide text-lavender-700">FemAI summary</p>
              <p>{summary}</p>
            </div>
          </Card>
        </section>

        {/* Right Column */}
        <section className="space-y-4">
          <Card title="FemAI archetype">
            <p className="text-lg font-semibold text-lavender-700">{archetype.label}</p>
            <p className="text-sm text-slate-700">{archetype.description}</p>
          </Card>

          <Card title="Daily tip">
            <p className="text-sm text-slate-700">{dailyTip(profile.currentPhase, profile)}</p>
          </Card>

          <Card title="Productivity suggestion">
            <p className="text-sm text-slate-700">{productivitySuggestion(profile.currentPhase)}</p>
          </Card>

          <Card title="Budget insight">
            <p className="text-sm text-slate-700">{budgetInsight(profile.monthlyBudget, profile)}</p>
          </Card>
        </section>
      </div>
    </div>
  );
}
