import {
  AIConfigEditor,
  type AIConfigCallbacks,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";
import APITokenInput from "./APITokenInput";
import { Flex, MantineProvider, type MantineTheme } from "@mantine/core";
import WorkbookInfoAlert from "./WorkbookInfoAlert";
import { useMemo } from "react";

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

  const theme = useMemo(
    () => ({
      colorScheme: themeMode,
      defaultGradient: {
        from: "#E88949",
        to: "#E85921",
        deg: 90,
      },
      globalStyles: (theme: MantineTheme) => {
        const inputBorderColor =
          theme.colorScheme === "light" ? "#E5E7EB" : "#384152";
        const inputBackgroundColor =
          theme.colorScheme === "light" ? "white" : "#374151";

        return {
          "div.editorBackground": {
            background: theme.colorScheme === "light" ? "white" : "#0b0f19",

            ".mantine-Input-input": {
              border: `1px solid ${inputBorderColor} !important`,
              boxShadow: "0px 1px 4px 0px rgba(0, 0, 0, 0.05) inset",
              backgroundColor: inputBackgroundColor,
              ":focus": {
                outline: "solid 1px #E85921 !important",
                outlineOffset: "-1px",
              },
            },
          },
        };
      },
    }),
    [themeMode]
  );

  return (
    <MantineProvider withGlobalStyles withNormalizeCSS theme={theme}>
      <div className="editorBackground">
        <Flex direction="column" p="0 1rem" mt="1rem">
          <WorkbookInfoAlert />
          <APITokenInput onSetToken={props.onSetApiToken} />
        </Flex>
        <AIConfigEditor
          callbacks={props.editorCallbacks}
          aiconfig={props.aiconfig}
          mode="gradio"
          themeMode={themeMode}
        />
      </div>
    </MantineProvider>
  );
}
