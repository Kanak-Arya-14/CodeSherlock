import { motion } from "framer-motion";

interface Props {
  title: string;
  children: React.ReactNode;
}

export default function SectionCard({
  title,
  children,
}: Props) {
  return (
    <motion.div
      initial={{
        opacity: 0,
        y: 20,
      }}
      animate={{
        opacity: 1,
        y: 0,
      }}
      className="
      bg-slate-900
      border
      border-slate-800
      rounded-3xl
      p-8
      shadow-xl
      "
    >
      <h2 className="text-2xl font-bold mb-6">
        {title}
      </h2>

      {children}
    </motion.div>
  );
}