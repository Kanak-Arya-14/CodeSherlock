import { motion } from "framer-motion";
import type { LucideIcon } from "lucide-react";

interface Props {
  icon: LucideIcon;
  title: string;
  value: string | number;
}

export default function StatCard({
  icon: Icon,
  title,
  value,
}: Props) {
  return (
    <motion.div
      whileHover={{
        y: -6,
        scale: 1.02,
      }}
      className="rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-xl"
    >
      <div className="flex items-center gap-3 text-slate-400">
        <Icon size={22} />
        <span>{title}</span>
      </div>

      <h2 className="text-3xl font-bold mt-4">
        {value}
      </h2>
    </motion.div>
  );
}