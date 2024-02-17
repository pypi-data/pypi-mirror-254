; ModuleID = 'ghz_fail.bc'
source_filename = "LLVMDialectModule"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%Qubit = type opaque
%Result = type opaque

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__rt__result_record_output(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__array_end_record_output() local_unnamed_addr

declare void @__quantum__rt__array_start_record_output() local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

define void @__nvqpp__mlirgen__ghz() local_unnamed_addr #0 !dbg !3 {
  tail call void @__quantum__qis__h__body(%Qubit* null), !dbg !7
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*)), !dbg !9
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*)), !dbg !9
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null), !dbg !10
  %1 = tail call i1 @__quantum__qis__read_result__body(%Result* null), !dbg !11
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*)), !dbg !10
  %2 = tail call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*)), !dbg !11
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*)), !dbg !10
  %3 = tail call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*)), !dbg !11
  tail call void @__quantum__rt__array_start_record_output(), !dbg !12
  tail call void @__quantum__rt__result_record_output(%Qubit* null), !dbg !12
  tail call void @__quantum__rt__result_record_output(%Qubit* nonnull inttoptr (i64 1 to %Qubit*)), !dbg !12
  tail call void @__quantum__rt__result_record_output(%Qubit* nonnull inttoptr (i64 2 to %Qubit*)), !dbg !12
  tail call void @__quantum__rt__array_end_record_output(), !dbg !12
  ret void, !dbg !12
}

attributes #0 = { "EntryPoint" "requiredQubits"="3" "requiredResults"="3" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!2}

!0 = distinct !DICompileUnit(language: DW_LANG_C, file: !1, producer: "mlir", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug)
!1 = !DIFile(filename: "LLVMDialectModule", directory: "/")
!2 = !{i32 2, !"Debug Info Version", i32 3}
!3 = distinct !DISubprogram(name: "__nvqpp__mlirgen__ghz", linkageName: "__nvqpp__mlirgen__ghz", scope: null, file: !4, line: 1, type: !5, scopeLine: 1, spFlags: DISPFlagDefinition | DISPFlagOptimized, unit: !0, retainedNodes: !6)
!4 = !DIFile(filename: "-", directory: "/workspaces/qoda/qppOnlyBuild")
!5 = !DISubroutineType(types: !6)
!6 = !{}
!7 = !DILocation(line: 10, column: 3, scope: !8)
!8 = !DILexicalBlockFile(scope: !3, file: !4, discriminator: 0)
!9 = !DILocation(line: 32, column: 9, scope: !8)
!10 = !DILocation(line: 48, column: 11, scope: !8)
!11 = !DILocation(line: 0, scope: !8)
!12 = !DILocation(line: 54, column: 3, scope: !8)
