import {
  AIConfigEditor,
  type AIConfigCallbacks,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";
import APITokenInput from "./APITokenInput";

type Props = {
  aiconfig: AIConfig;
  editorCallbacks: AIConfigCallbacks;
  onSetApiToken: (apiToken: string) => Promise<void>;
  themeMode: "light" | "dark" | "system";
};

export default function GradioWorkbook(props: Props) {
  // AIConfigEditor handles dynamic system theme switching by default, so only
  // pass dark or light override
  const themeMode = props.themeMode === "system" ? undefined : props.themeMode;
  return (
    <div>
      <APITokenInput onSetToken={props.onSetApiToken} />
      <AIConfigEditor
        callbacks={props.editorCallbacks}
        aiconfig={props.aiconfig}
        mode="gradio"
        themeMode={themeMode}
      />
    </div>
  );
}
