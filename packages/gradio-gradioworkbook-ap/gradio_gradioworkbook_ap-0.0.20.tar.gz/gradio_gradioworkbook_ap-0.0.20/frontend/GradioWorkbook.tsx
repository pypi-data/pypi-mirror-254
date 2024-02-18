import {
  AIConfigEditor,
  type AIConfigCallbacks,
  type LogEvent,
  type LogEventData,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";
import APITokenInput from "./APITokenInput";
import { useCallback, useEffect } from "react";
import { datadogLogs } from "@datadog/browser-logs";

type Props = {
  aiconfig: AIConfig;
  editorCallbacks: AIConfigCallbacks;
  onSetApiToken: (apiToken: string) => Promise<void>;
  themeMode: "light" | "dark" | "system";
};

const MODE = "gradio";

export default function GradioWorkbook(props: Props) {
  // AIConfigEditor handles dynamic system theme switching by default, so only
  // pass dark or light override
  const themeMode = props.themeMode === "system" ? undefined : props.themeMode;

  const setupTelemetry = useCallback(async () => {
    // skip aiconfigrc check in gradio; enable telemetry by default.
    // yarn build/dev will set this environment variable
    const isDev = (process.env.NODE_ENV ?? "development") === "development";
    console.log("isDev:", isDev);

    datadogLogs.init({
      clientToken: "pub356987caf022337989e492681d1944a8",
      env: process.env.NODE_ENV ?? "development",
      service: "aiconfig-editor",
      site: "us5.datadoghq.com",
      forwardErrorsToLogs: true,
      sessionSampleRate: 100,
    });

    datadogLogs.setGlobalContextProperty('mode', MODE);
    
  }, []);
  useEffect(() => {
    setupTelemetry();
  }, [setupTelemetry]);

  const logEventHandler = useCallback(
    (event: LogEvent, data?: LogEventData) => {
      try {
        datadogLogs.logger.info(event, data);
      } catch (e) {
        // Ignore logger errors for now
      }
    },
    []
  );

  const callbacks = {
    ...props.editorCallbacks,
    logEvent: logEventHandler,
  }

  
  return (
    <div>
      <APITokenInput onSetToken={props.onSetApiToken} />
      <AIConfigEditor
        callbacks={callbacks}
        aiconfig={props.aiconfig}
        mode={MODE}
        themeMode={themeMode}
      />
    </div>
  );
}
