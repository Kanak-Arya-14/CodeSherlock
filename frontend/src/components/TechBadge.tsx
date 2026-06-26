import { motion } from "framer-motion";

interface Props {
  name: string;
}

export default function TechBadge({
  name,
}: Props) {
  return (
    <motion.span
      whileHover={{
        scale: 1.08,
      }}
      className="
      inline-flex
      px-4
      py-2
      rounded-full
      bg-blue-500/10
      border
      border-blue-500/40
      text-blue-300
      text-sm
      mr-3
      mb-3
      "
    >
      {name}
    </motion.span>
  );
}